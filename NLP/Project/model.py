import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score,confusion_matrix
import pickle



nltk.download("punkt_tab")
nltk.download("punkt")
nltk.download("stopwords")
nltk.download("wordnet")
nltk.download("averaged_perceptron_tagger_eng")

df=pd.read_csv("spam.csv")
print(df.info())
print(df.head(5))

df.rename(columns={
    "v1":"Label",
    "v2":"message"
},inplace=True)

print(df.columns)
print(df.isnull().sum())
print(df.describe)
#lower Case
df["message"]=df["message"].apply(lambda x:x.lower())
print(df["Label"].value_counts())



#Word Tokenzier
word_tokenize=[]
for message in df["message"]:
    word=nltk.word_tokenize(message)
    word_tokenize.append(word)


#stop words
stop_word=stopwords.words("english")

lemmatizer=WordNetLemmatizer()
processed_message=[]
for word in word_tokenize:
    filtered_word=[]
    for w in word:
        if w not in stop_word:
            filtered_word.append(w)
    
    

    #stemming
    lemma=[]

    for w in filtered_word:
        pos_tag=nltk.pos_tag([w])
        pos=pos_tag[0][1]
        if pos.startswith("V"):
            pos = "v"
        elif pos.startswith("N"):
            pos = "n"
        elif pos.startswith("J"):
            pos = "a"
        elif pos.startswith("R"):
            pos = "r"
        else:
            pos = "n" 
        lemma.append(lemmatizer.lemmatize(w,pos=pos))

    clean_message = " ".join(lemma)
    processed_message.append(clean_message)

df["processed_message"]=processed_message
x=df["processed_message"]
y=df["Label"]

tfidf=TfidfVectorizer()
x=tfidf.fit_transform(x)

x_train,x_temp,y_train,y_temp=train_test_split(x,y,train_size=0.7,random_state=46)
x_val,x_test,y_val,y_test=train_test_split(x_temp,y_temp,test_size=0.5,random_state=46)
model=MultinomialNB()
model.fit(x_train,y_train)

predict=model.predict(x_test)

ac=accuracy_score(y_test,predict)
print(ac)
print(confusion_matrix(y_test,predict))
print(x.shape)


with open("model.pkl","wb") as file:
    pickle.dump(model,file)

with open("tfidf.pkl","wb") as file:
    pickle.dump(tfidf,file)
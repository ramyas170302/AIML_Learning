import nltk
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

nltk.download('words')
nltk.download("punkt")
nltk.download("averaged_perceptron_tagger")
nltk.download("maxent_ne_chunker")
nltk.download("words")

corpus = "John works at Google in Bengaluru. Sarah visited Microsoft in Delhi."
#sentence tokenize
sen=sent_tokenize(corpus)
print("Sentence tokenize:")
print(sen)
print("\n")

# word tokenize
words=word_tokenize(corpus)
print("word tokenize:")
print(words)
print("\n")

#stop word removal
stop_words=stopwords.words("english")
print("stop_words are:")
print(stop_words)
print("\n")


#remove stop words:
non_stop_words=[]
for word in words:
    if word not in stop_words:
        non_stop_words.append(word)
print("After stop words remove:")
print(non_stop_words)
print("\n")

#Lemmatization
lemmatizer=WordNetLemmatizer()
stemming=[]

for word in non_stop_words:
    pos_tag=nltk.pos_tag([word])
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
    stemming.append(lemmatizer.lemmatize(word.lower(),pos=pos))
print("Lemma:")
for lemma in stemming:
    print(lemma)


# NER
tags=nltk.pos_tag(words)
entities=nltk.ne_chunk(tags)
print(entities)







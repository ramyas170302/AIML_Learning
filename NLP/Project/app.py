import streamlit as st
import pickle
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


model=pickle.load(open("model.pkl","rb"))
tfidf=pickle.load(open("tfidf.pkl","rb"))


st.header("Spam Message Detector")
st.write("Enter a message below to check whether it is Spam or Ham.")

message=st.text_area("Enter the message",height=150,placeholder="Type or paste your message here...")

if st.button("Predict"):
    if message.strip()=="":
        st.warning("Please enter a message.")
    else:
        st.write("Character:",len(message))
        st.write("Words:",len(message.split()))

        #lowercase 
        message=message.lower()

        #word tokenization
        words=nltk.word_tokenize(message)

        #remove stop words
        filter_words=[]
        stop_word=stopwords.words("english")
        for word in words:
            if word not in stop_word:
                filter_words.append(word)

        lemma=[]
        lemmatizer=WordNetLemmatizer()
        for word in filter_words:
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

            lemma.append(lemmatizer.lemmatize(word, pos))

        clean_message=" ".join(lemma)
        vector=tfidf.transform([clean_message])

        #prediction
        predicition=model.predict(vector)

       

        if predicition[0]=="spam":
            st.error("Spam Message")
        else:
            st.success("Ham message")
      
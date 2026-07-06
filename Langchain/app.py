from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import HumanMessage,AIMessage

import streamlit as st 
import os
from dotenv import load_dotenv

load_dotenv()

llm=ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")
)
st.title("Simple Chatbot")
question=st.text_input("Enter question")
prompt=ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful AI assistant. Answer in simple English."),
        ("human", "{question}")
    ]
)
parse=StrOutputParser()
chain=prompt|llm|parse


#question=input("You:")
if st.button("Answer"):
    if(question):
        response=chain.invoke(
            {
                "question":question
            }
        )
        st.write(response)
    else:
        st.warning("Please enter a question!")





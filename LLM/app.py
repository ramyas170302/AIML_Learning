'''from dotenv import load_dotenv
import os
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
#print(api_key)
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=api_key
)
response = llm.invoke(
    """
    Explain AI in simple English.

    Give:
    - Definition
    - Real-life example
    - Advantages

    Keep the answer under 100 words.
    """
)

print(response.content)
print(type(response))
print(response.usage_metadata)'''
from langchain_community.document_loaders import PyPDFLoader
loader = PyPDFLoader("pdfs/python.pdf")
documents = loader.load()
print(type(documents))
print(len(documents))
print(documents[0].page_content)
print(documents[0].metadata)
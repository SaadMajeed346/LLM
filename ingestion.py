import os
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import  CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings


load_dotenv()
if __name__ == "__main__":
    print(f"started")

import os
from dotenv import load_dotenv

if __name__ == "__main__":
    load_dotenv()
    print('Hello LangChain')
    print(os.environ['OPEN_API_KEY'])

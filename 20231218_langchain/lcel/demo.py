from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser, MarkdownListOutputParser
from dotenv import load_dotenv, find_dotenv
import os

_ = load_dotenv(find_dotenv())

BASE_URL = os.environ.get("BASE_URL")
API_KEY = os.environ.get("API_KEY")

print(BASE_URL)
print(API_KEY)

prompt = ChatPromptTemplate.from_template("tell me a short joke about {topic}")
model = ChatOpenAI(
    openai_api_key=API_KEY,
    base_url=BASE_URL,
)
output_parser = StrOutputParser()

chain = prompt | model | output_parser

resp = chain.invoke({"topic": "ice cream"})
print(type(resp))
print(resp)

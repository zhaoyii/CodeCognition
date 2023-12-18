from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage
import os
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

BASE_URL = os.environ.get("BASE_URL")
API_KEY = os.environ.get("API_KEY")

print(BASE_URL)
print(API_KEY)

llm = OpenAI(
    openai_api_key=API_KEY,
    base_url=BASE_URL,
)


text = "What would be a good company name for a company that makes colorful socks?"
messages = [HumanMessage(content=text)]
print(llm.invoke(text))
# >> Colorful Sock Co.

chat_model = ChatOpenAI(
    openai_api_key=API_KEY,
    base_url=BASE_URL,
)

print(chat_model.invoke(messages))
# >> AIMessage(content="Socks O'Color")

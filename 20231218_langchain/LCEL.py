from typing import List

from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema import BaseOutputParser
import os
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

BASE_URL = os.environ.get("BASE_URL")
API_KEY = os.environ.get("API_KEY")

print(BASE_URL)
print(API_KEY)


class CommaSeparatedListOutputParser(BaseOutputParser[List[str]]):
    """Parse the output of an LLM call to a comma-separated list."""

    def parse(self, text: str) -> List[str]:
        """Parse the output of an LLM call."""
        return text.strip().split(", ")


template = """You are a helpful assistant who generates comma separated lists.
A user will pass in a category, and you should generate 5 objects in that category in a comma separated list.
ONLY return a comma separated list, and nothing more."""
human_template = "{text}"

chat_prompt = ChatPromptTemplate.from_messages([
    ("system", template),
    ("human", human_template),
])

chat_model = ChatOpenAI(
    openai_api_key=API_KEY,
    base_url=BASE_URL,
)

chain = chat_prompt | chat_model | CommaSeparatedListOutputParser()
resutls = chain.invoke({"text": "colors"})
print(resutls)
# >> ['red', 'blue', 'green', 'yellow', 'orange']

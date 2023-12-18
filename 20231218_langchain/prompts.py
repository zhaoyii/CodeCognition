from langchain.prompts import PromptTemplate

prompt = PromptTemplate.from_template("What is a good name for a company that makes {product}?")
p = prompt.format(product="colorful socks")

print(p)


from langchain.prompts.chat import ChatPromptTemplate

template = "You are a helpful assistant that translates {input_language} to {output_language}."
human_template = "{text}"

chat_prompt = ChatPromptTemplate.from_messages([
    ("system", template),
    ("human", human_template),
])

ls = chat_prompt.format_messages(input_language="English", output_language="French", text="I love programming.")

for e in ls:
    print(e)
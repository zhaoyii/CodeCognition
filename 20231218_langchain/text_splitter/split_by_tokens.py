# This is a long document we can split up.
from langchain.text_splitter import CharacterTextSplitter

with open("state_of_the_union.txt", encoding="utf-8") as f:
    state_of_the_union = f.read()



text_splitter = CharacterTextSplitter.from_tiktoken_encoder(
    chunk_size=100, chunk_overlap=0
)
texts = text_splitter.split_text(state_of_the_union)


print(texts[0]) # raw txt
print(len(texts[0])) # len of txt
print()
print(texts[0].split(" "))
print(len(texts[0].split(" "))) # words 
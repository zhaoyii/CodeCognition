"""
对于一般文本，推荐使用此文本拆分器。

它由字符列表参数化。它尝试按顺序分割它们，直到块足够小。默认列表为 ["\n\n", "\n", " ", ""]。

这样做的效果是尝试将所有段落（然后是句子，然后是单词）尽可能长时间地放在一起，因为这些通常看起来是语义相关性最强的文本片段。

1.文本如何分割：按字符列表。
2.如何测量块大小：按字符数。
"""

from langchain.text_splitter import RecursiveCharacterTextSplitter

# This is a long document we can split up.
with open('state_of_the_union_chinese2.txt', encoding="utf-8") as f:
    state_of_the_union = f.read()

text_splitter = RecursiveCharacterTextSplitter(
    # Set a really small chunk size, just to show.
    chunk_size = 1000,
    chunk_overlap  = 200,
    length_function = len,
    is_separator_regex = False,
)

texts = text_splitter.create_documents([state_of_the_union])

print(texts[0])
print(len(texts[0].page_content))
print(texts[1])
print(len(texts[1].page_content))
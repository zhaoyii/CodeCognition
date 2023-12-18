from langchain.text_splitter import MarkdownHeaderTextSplitter


with open('example.md', encoding="utf-8") as f:
    markdown_document = f.read()
    
headers_to_split_on = [
    ("#", "Header 1"),
    ("##", "Header 2"),
    ("###", "Header 3"),
]

markdown_splitter = MarkdownHeaderTextSplitter(headers_to_split_on=headers_to_split_on)
md_header_splits = markdown_splitter.split_text(markdown_document)
# print(md_header_splits)

print(md_header_splits[0].page_content)
print()
print(md_header_splits[1].page_content)
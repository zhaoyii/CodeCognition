import spacy

# 1. 加载预训练模型
nlp = spacy.load("en_core_web_md")

# 2. 处理文本
text = "Spacy is a fantastic library for NLP tasks!"
doc = nlp(text)

# 3. 获取每个词的向量并打印
for token in doc:
    print(f"Token: {token.text}")
    print(f"Vector (First 5 dimensions): {token.vector}")
    print("------")

# 4. 如果你只想获取特定词的向量，可以这样做：
word = "Spacy"
vector = nlp(word).vector
print(f"Vector for '{word}' (First 5 dimensions): {vector}")

from transformers import pipeline
from dotenv import load_dotenv, find_dotenv
import os

_ = load_dotenv(find_dotenv())

# 设置代理
http_proxy = os.getenv("HTTP_PROXY")
https_proxy = os.getenv("HTTPS_PROXY")
if http_proxy:
    os.environ["http_proxy"] = http_proxy
if https_proxy:
    os.environ["https_proxy"] = https_proxy

# pipeline 创建一个 Pipeline 对象
# classifier 是一个 Pipeline 对象
classifier = pipeline(task="sentiment-analysis",
                      model="distilbert-base-uncased-finetuned-sst-2-english",
                      device=-1) # 使用 CPU 运行模型

# 把 Pipeline 对象当做函数执行，最终执行 Pipeline 对象的 __call__() 方法
# Pipeline 对象称之为“可执行对象”（callable objects）
result = classifier("We are very happy to show you the 🤗 Transformers library.")
print(result) # [{'label': 'POSITIVE', 'score': 0.9997795224189758}]

results = classifier(["We are very happy to show you the 🤗 Transformers library.", "We hope you don't hate it."])
print(results) # [{'label': 'POSITIVE', 'score': 0.9997795224189758}, {'label': 'NEGATIVE', 'score': 0.5308612585067749}]

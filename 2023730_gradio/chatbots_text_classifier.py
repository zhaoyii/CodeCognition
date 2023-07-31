from transformers import pipeline
from dotenv import load_dotenv, find_dotenv
import gradio as gr

_ = load_dotenv(find_dotenv())

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


def chat_classifier(message, history):
    print(message)
    print(history)
    result = classifier(message)
    r = result[0]
    return f'label={r["label"]} score={r["score"]}'

demo = gr.ChatInterface(chat_classifier)

demo.launch()
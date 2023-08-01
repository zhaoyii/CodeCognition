from transformers import AutoTokenizer, AutoModel
from dotenv import load_dotenv, find_dotenv
import gradio as gr

_ = load_dotenv(find_dotenv())


tokenizer = AutoTokenizer.from_pretrained("THUDM/chatglm2-6b", trust_remote_code=True)
model = AutoModel.from_pretrained("THUDM/chatglm2-6b", trust_remote_code=True).half().cuda()
model = model.eval()

response, history = model.chat(tokenizer, "你好", history=[])
print(response)
response, history = model.chat(tokenizer, "晚上睡不着应该怎么办", history=history)
print(response)

def chatbots(message, history):
    response, history = model.chat(tokenizer, message, history=history)
    return response

demo = gr.ChatInterface(chatbots)

demo.launch()

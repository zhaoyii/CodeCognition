"""
聊天机器人

Gradio 包含一个高级类，gr.ChatInterface，它与 gr.Interface 类似，
但专为聊天机器人用户界面而设计。gr.ChatInterface 类同样包装一个函数，
但这个函数必须有一个特定的签名。这个函数应该接受两个参数：消息和历史（参数可以任意命名，但必须按此顺序）

消息（message）：代表用户输入的字符串
历史（history）：代表到那个时刻为止的对话的列表。每个内部列表由两个字符串组成，表示一对：[用户输入，机器人响应]。
你的函数应该返回一个单一的字符串响应，这是机器人对特定用户输入消息的响应。

除此之外，gr.ChatInterface 没有必需的参数（尽管有很多可用于自定义用户界面的参数）。
"""

import random
import gradio as gr

def random_response(message, history):
    return random.choice(["Yes", "No"])

demo = gr.ChatInterface(random_response)

demo.launch()
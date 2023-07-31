"""
区块：更多的灵活性和控制
Gradio 提供了两种构建应用程序的方法：

1. Interface 和 ChatInterface，为我们迄今为止讨论的创建演示提供了高级抽象。

2. 区块（Blocks），这是一个用于设计具有更灵活布局和数据流的web应用程序的低级API。
区块允许你做诸如特性多个数据流和演示、控制组件在页面上的出现位置、处理复杂的数据流
（例如，输出可以作为其他函数的输入），以及基于用户交互更新组件的属性/可见性 —— 全部
仍然在Python中完成。如果你需要这种可定制性，请尝试使用区块！

需要注意的事项：

区块是使用 with 语句创建的，任何在此语句内创建的组件都会自动添加到应用程序中。
组件在应用中按照它们被创建的顺序垂直显示。（稍后我们将讨论如何自定义布局！）
一个按钮被创建，然后给这个按钮添加了一个点击事件监听器。这个API应该看起来很熟悉！
就像 Interface 一样，click 方法需要一个Python函数、输入组件和输出组件。
"""

import gradio as gr

def greet(name):
    return "Hello " + name + "!"

with gr.Blocks() as demo:
    name = gr.Textbox(label="Name")
    output = gr.Textbox(label="Output Box")
    greet_btn = gr.Button("Greet")
    greet_btn.click(fn=greet, inputs=name, outputs=output, api_name="greet")

demo.launch()
import gradio as gr

def greet(name):
    return "Hello " + name + "!"

"""
gr.Interface 这个接口类可以为任何 Python 函数提供用户界面（UI）。

在上面的例子中，我们看到了一个简单的基于文本的函数，但这个函数可以是从音乐生成器到税务计算器，再到预训练机器学习模型的预测功能。

核心的接口类在初始化时需要三个必需的参数：

fn：需要围绕其创建UI的函数
inputs：用于输入的组件（例如“文本”、“图片”或“音频”）
outputs：用于输出的组件（例如“文本”、“图片”或“标签”）
让我们更仔细地看看这些用于提供输入和输出的组件。
"""
demo = gr.Interface(fn=greet, inputs="text", outputs="text")
    
demo.launch(share=True)  
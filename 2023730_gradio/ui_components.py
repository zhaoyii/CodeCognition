"""
UI components 组件属性

在之前的示例中，我们看到了一些简单的文本框组件，但如果您想改变 UI 组件的外观或行为怎么办？

假设您想自定义输入文本字段 —— 例如，您希望它更大并带有文本占位符。
如果我们使用Textbox的实际类，而不是使用字符串快捷方式，

那么通过组件属性，您可以获得更多的自定义功能。
"""
import gradio as gr

def greet(name):
    return "Hello " + name + "!"

demo = gr.Interface(
    fn=greet,
    inputs=gr.Textbox(lines=2, placeholder="Name Here..."),
    outputs="text",
)
demo.launch()
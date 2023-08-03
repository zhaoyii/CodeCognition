"""
【开发流程】

每次你想更新你的应用程序，保存源文件。当你这样做时，Streamlit会检测是否有变化，
并询问你是否希望重新运行你的应用程序。在屏幕的右上角选择“始终重新运行”，这样每
次更改源代码时，你的应用程序都会自动更新。

这允许你在一个快速的交互循环中工作：你键入一些代码，保存它，实时尝试它，然后键入
更多的代码，保存它，尝试它，等等，直到你对结果满意为止。这种在编码和实时查看结果
之间的紧密循环是Streamlit使你的生活变得更加轻松的方式之一。

【⭐提示】
在开发Streamlit应用程序时，建议将你的编辑器和浏览器窗口并排放置，这样可以同时查看
代码和应用程序。试试看！

从Streamlit版本1.10.0及更高版本开始，不能从Linux发行版的根目录运行Streamlit应用
程序。如果你尝试从根目录运行Streamlit应用程序，Streamlit会抛出一个FileNotFoundError: [Errno 2] No such file or directory
错误。有关更多信息，请查看GitHub问题#5239。

如果你正在使用Streamlit版本1.10.0或更高版本，你的主脚本应该位于根目录之外的目录中。
使用Docker时，你可以使用WORKDIR命令来指定主脚本所在的目录。要了解如何做到这一点，请阅读创建Dockerfile。

【数据流】

Streamlit的架构允许你像编写普通Python脚本一样编写应用程序。为了解锁这一点，Streamlit
应用程序有一个独特的数据流：每当屏幕上的某个东西必须更新时，Streamlit会从头到尾重新运
行你的整个Python脚本。

这可能发生在两种情况下：

- 每当你修改应用程序的源代码时。
- 每当用户与应用中的小部件进行交互。例如，当拖动滑块、在输入框中输入文本或点击按钮时。

每当通过on_change（或on_click）参数将回调传递给小部件时，回调将始终在脚本的其余部分之前
运行。有关回调API的详细信息，请参考我们的会话状态API参考指南。

为了使所有这些快速无缝，Streamlit在幕后为你做了一些繁重的工作。这个故事中的一个重要角色
是@st.cache_data修饰器，它允许开发人员在应用程序重新运行时跳过某些昂贵的计算。稍后我们
将在这个页面上讲解缓存。

运行程序命令：streamlit run magic.py
"""

import streamlit as st
import pandas as pd
import numpy as np

'''
Use magic - 使用魔法
'''
df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

df

'''
Write a data frame - 编写数据框架
'''
st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))

dataframe = np.random.randn(10, 20)
st.dataframe(dataframe)


dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))

st.dataframe(dataframe.style.highlight_max(axis=0))

dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))
st.table(dataframe)


'''
Draw charts - 绘制图表
'''
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)


'''
Plot a map - 绘制地图
'''
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)
import streamlit as st
import numpy as np
import pandas as pd

"""
当你已经有了希望探索的数据或模型时，你可以加入像 st.slider()、st.button() 
或 st.selectbox() 这样的小部件。这真的很简单 —— 将小部件视为变量：

在首次运行上述应用时，应该输出文本“0的平方是0”。然后，每当用户与一个小部件进行
交互时，Streamlit 会简单地从头到尾重新运行你的脚本，并在过程中将小部件的当前状态
分配给你的变量。

例如，如果用户将滑块移动到10的位置，Streamlit 将重新运行上面的代码并相应地将 x 设
置为10。因此，现在你应该看到的文本是“10的平方是100”。
"""

x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)

st.text_input("Your name", key="name")
# You can access the value at any point with:
st.session_state.name


'''
使用复选框来显示/隐藏数据
复选框的一个使用场景是在应用中隐藏或显示特定的图表或部分。st.checkbox() 取一个参数，
即小部件的标签。在这个示例中，复选框被用来切换一个条件语句。
'''
if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data


'''
使用选择框选择选项
使用 st.selectbox 从系列中进行选择。你可以编写你想要的选项，或者传递一个数组或数据帧列。
'''

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })

option = st.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected: ', option
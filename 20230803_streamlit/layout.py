
"""
布局

Streamlit 使得在左侧面板边栏中组织你的小部件变得非常容易，可以使
用 st.sidebar。传递给 st.sidebar 的每个元素都被固定在左侧，允许
用户专注于应用中的内容，同时仍然可以访问用户界面控制。

例如，如果你想在边栏中添加一个选择框和一个滑块，使用 st.sidebar.slider 
和 st.sidebar.selectbox，而不是 st.slider 和 st.selectbox：
"""

import streamlit as st
import time

# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)


'''
除了侧边栏，Streamlit 还提供了几种其他方法来控制你应用的布局。st.columns
 允许你将小部件并排放置，而 st.expander 可以通过隐藏大内容来节省空间。
'''
left_column, right_column = st.columns(2)
# You can use a column just like st.sidebar:
left_column.button('Press me!')

# Or even better, call Streamlit functions inside a "with" block:
with right_column:
    chosen = st.radio(
        'Sorting hat',
        ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
    st.write(f"You are in {chosen} house!")

'''
显示进度

当在应用中添加长时间运行的计算时，你可以使用 st.progress() 来实时显示状态。

首先，让我们导入 time。我们将使用 time.sleep() 方法来模拟一个长时间运行的计算：
'''


'Starting a long computation...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

'...and now we\'re done!'
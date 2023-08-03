"""
运行多页面应用

运行多页面应用与运行单页面应用相同。运行多页面应用的命令是：

streamlit run [入口文件]

"入口文件" 是应用向用户显示的第一个页面。一旦你为应用添加了页面，
入口文件会出现在边栏的最顶部。你可以把入口文件视为应用的“主页面”。
例如，假设你的入口文件是 Home.py。那么，要运行你的应用，你可以
运行 streamlit run Home.py。这将启动你的应用并执行 Home.py 中的代码。


Home.py # This is the file you run with "streamlit run"
└─── pages/
  └─── About.py # This is a page
  └─── 2_Page_two.py # This is another page
  └─── 3_😎_three.py # So is this
"""

import streamlit as st

st.markdown("# Main page 🎈")
st.sidebar.markdown("# Main page 🎈")

st.markdown("# Page 2 ❄️")
st.sidebar.markdown("# Page 2 ❄️")

st.markdown("# Page 3 🎉")
st.sidebar.markdown("# Page 3 🎉")
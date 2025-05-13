# im learning streamlit. it's hello world with YT and their get started
# https://www.youtube.com/watch?v=d7fnzDQ5qM8

import numpy as np
import pandas as pd
import streamlit as st

st.title("streamlit hello world st.title")

with st.sidebar:
    st.header("About app")
    st.write("this is my first app page?")

st.header("this is a st.header ")
st.markdown("write text as st.markdown *with* fancy ***formating*** [ya.ru](ya.ru)")
# st.write("hello world")

st.subheader("st.column + st.slider + st.write")
col1, col2 = st.columns(2)
with col1:
    x = st.slider("Choose and x value", 1, 10)
with col2:
    st.write("the value of :blue[***x***] is", x, "to change color \:blue[text]")


st.subheader("st.area_chart")

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
st.area_chart(chart_data)

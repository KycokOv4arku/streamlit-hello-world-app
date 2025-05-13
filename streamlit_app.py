# im learning streamlit. it's hello world with YT and their get started
# https://www.youtube.com/watch?v=d7fnzDQ5qM8

import numpy as np
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="kckv4rk streamlit Hello World",
    page_icon="🐍",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={
        "About": "Learning how to use Streamlit basics - widgets, charts, layout, etc."
    },
)

st.title("streamlit hello world st.title")

st.write("hello world")

with st.sidebar:
    st.header("About app")
    st.write("this is my first app page?")

st.header("this is a st.header ")
st.markdown("write text as st.markdown *with* fancy ***formating*** [ya.ru](ya.ru)")


st.subheader("st.column + st.slider + st.write")
# split everything into 2 columns
col1, col2 = st.columns(2)
with col1:
    # add widget
    x = st.slider("Choose and x value", 1, 10)
with col2:
    st.write("the value of :blue[***x***] is", x, r"to change color :blue[text]")


# lets go through docs/basic concepts
# https://docs.streamlit.io/get-started/fundamentals/main-concepts

# u can run github gists 'streamlit run url_file_py
# https://raw.githubusercontent.com/KycokOv4arku/streamlit-hello-world-app/refs/heads/master/streamlit_app.py

# each time u change script or interact with an app. script is rerun.
# so explore @st.cache_data decorator. they promote it

# magic
st.subheader("magic. when we dont even use st.write()")
st.write("works when streamlit sees a single variable or a literal value on its own line")
df = pd.DataFrame({"first column": [1, 2, 3, 4], "second column": [10, 20, 30, 40]})
df
"i am text string on its own line witout any methods used on me"

# swiss knife st.write()
st.subheader("Same yet with st.write()")
st.write(pd.DataFrame({"first column": [1, 2, 3, 4], "second column": [10, 20, 30, 40]}))

# static table
st.subheader("make a table static st.table(df)")
st.table(df)

# customize table
st.subheader("customize table with pandas style")
dataframe = pd.DataFrame(
    np.random.randn(10, 20), columns=("col %d" % i for i in range(20))
)
st.dataframe(dataframe.style.highlight_max(axis=0))

# draw charts

st.subheader("st.area_chart()")
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
st.area_chart(chart_data)

st.subheader("st.line_chart()")
st.line_chart(chart_data)

st.subheader("st.map() numpy generates 1000 points around Moscow coords")
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [10, 10] + [55.7558, 37.6173], columns=["lat", "lon"]
)
st.map(map_data)

# widgets
st.subheader("another widget")
col2_1, col2_2 = st.columns(2)
with col2_1:
    y = st.slider("y", 1, 50)
with col2_2:
    st.write(y, "squared is", y * y)
# access by key
st.subheader(
    'access by key with st.text_input("text", key="name") and st.session_state.name'
)

st.text_input("Your name is", key="name")
name = st.session_state.name
st.write(f"Hello world{"" if not name else ', ' + name}!")

# checkboxes help show/hide data
st.subheader("to show/hide data checkbox helps")
if st.checkbox("Show dataframe"):
    chart_data
    "the code how it's done"
    st.markdown(
        "```python\n"
        "if st.checkbox('show dataframe'):\n"
        "    chart_data"  #
    )

# selectbox for options
st.subheader("selectbox for options")
df2 = pd.DataFrame({"first column": [1, 2, 3, 4], "second column": [10, 20, 30, 40]})
option = st.selectbox("Which number do you like best?", df2["first column"])
"You selected: ", option

import pandas as pd
import streamlit as st
import plotly.express as px
from streamlit_lottie import st_lottie  # pip install streamlit-lottie
import requests  # pip install requests


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


dataset = pd.read_excel('Managed Sellers DB.xlsx',
                        usecols='A:O')
dataset2 = pd.read_excel('Managed Sellers DB.xlsx',
                         usecols='Q:R')

# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Seller Dashboard", page_icon=":bar_chart:", layout="wide")

# Add logo or icon to the sidebar using a URL
st.sidebar.image("data/logo.png", caption="")
st.sidebar.header("Filter By")

csm = st.sidebar.multiselect("Filter By CSM:",
                             options=dataset["CSM"].unique(),
                             default=dataset["CSM"].unique())

selection_query = dataset.query(
    "CSM == @csm"
)

st.title("CSM Managed Sellers")
st.dataframe(selection_query)

vertical = st.sidebar.multiselect("Filter By Vertical:",
                                  options=dataset["Vertical"].unique(),
                                  default=dataset["Vertical"].unique())
st.title("Verticals by Percentage")
selection_query1 = dataset.query(
    "Vertical == @vertical"
)

st.dataframe(selection_query1)

# Check if the dataframe is empty:
if selection_query.empty:
    st.warning("No data available based on the current filter settings!")
    st.stop()  # This will halt the app from further execution.

lottie_hello = load_lottieurl("https://lottie.host/dd8faef9-7af7-46be-a2c1-51437c27a020/z6XPrkVaHm.json")

st_lottie(
    lottie_hello,
    speed=1,
    reverse=False,
    loop=True,
    quality="medium",
    height=450,
    width=1250,
    key="hello",
)

col1, col2 = st.columns(2)

pie_chart1 = px.pie(dataset2,
                    title='Sellers & Verticals',
                    values='Sellers',
                    names='Verticals')

col1.plotly_chart(pie_chart1)

pie_chart2 = px.pie(dataset,
                    title='Total Sellers GTV',
                    values='TTM GTV ($)',
                    names='Company ID')

col2.plotly_chart(pie_chart2)

# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

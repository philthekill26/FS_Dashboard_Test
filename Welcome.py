import streamlit as st
from streamlit_lottie import st_lottie  # pip install streamlit-lottie
import requests  # pip install requests


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


st.set_page_config(page_title="FastSpring Dashboard", page_icon=":bar_chart:", layout="wide")

st.title("Welcome!")
st.sidebar.success("Select a page above.")

st.write(
    """
Welcome to the FastSpring Managed Seller Dashboard here you can view the Main dashboard, view the Seller stats,
or Vertical stats.
"""
)

lottie_hello = load_lottieurl("https://lottie.host/8146da3c-fc9b-4b73-8579-f6f5b044057d/vTw8ApZy6D.json")

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
# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

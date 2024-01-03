import streamlit as st


st.set_page_config(page_title="FastSpring Dashboard", page_icon=":bar_chart:", layout="wide")

st.title("Vertical Stats")



# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
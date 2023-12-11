import streamlit as st

page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
background-image: url("https://i.imgur.com/fnCdgY6.png")
background-size: cover;
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html = True)

#import
import streamlit as st
from PIL import Image

#background
page_bg_img = '''<style>
[data-testid="stAppViewContainer"] {
background-color:#FFFFFF}
</style>'''
#page_bg_img = '''<style>
  [data-testid="stAppViewContainer"] {
    background-color:#FFFFFF}
      </style>'''
st.markdown(page_bg_img, unsafe_allow_html=True)
colT1, colT2 = st.columns([1, 5])
with colT2:

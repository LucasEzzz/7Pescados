#import
import streamlit as st
from PIL import Image

#background
page_bg_img = '''<style>
[data-testid="stAppViewContainer"] {
background-color:#FFFFFF}
</style>'''
st.markdown(page_bg_img, unsafe_allow_html=True)
colT1, colT2 = st.columns([5, 5])
with colT2:
  image = Image.open('project.png')
  st.image(image, width=400)

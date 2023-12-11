#import
import streamlit as st
#from PIL import Image

#background
#page_bg_img = '''<style>
#[data-testid="stAppViewContainer"] {
#background-color:#2B5DB9}
#</style>'''
#st.markdown(page_bg_img, unsafe_allow_html=True)
#colT1, colT2 = st.columns([5,5])
#with colT2:
  #image = Image.open('project2.jpeg')
  #st.image(image, width=3000)

page_bg_img = """
[data-testid="stAppViewContainer"] {
background-image: Image.open('project2.jpeg')
background-size: cover;
}
[data-testid="stHeader"]{
background-color: rgba(0, 0, 0, 0);
}
[data-testid="stToolbar"]{
right: 2rem;
}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)
st.title("It's summer!")

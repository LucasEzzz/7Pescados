import streamlit as st

# Importe a imagem
imagem = "https://i.imgur.com/fnCdgY6.png"

# Crie o código CSS
css = """
body {
  background-image: url({})
  background-size: cover;
  background-repeat: no-repeat;
}
""".format(imagem)

# Exiba o código CSS
st.markdown(css, unsafe_allow_html=True)

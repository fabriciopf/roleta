import streamlit as st
import random
from PIL import Image

st.set_page_config(page_title="Roleta de Filmes", page_icon="🎬", layout="centered")

st.title("Roleta de Filmes")
st.write("Clique no botão abaixo para rodar a roleta entre *Kung Fu Panda* e *Ratatouille*.")

if st.button("Rodar Roleta"):
    opcao = random.choice(["https://images.app.goo.gl/AvHxs", "https://m.media-amazon.com/images/I/81r+LN7kAfL._AC_UF894,1000_QL80_.jpg"])
    st.markdown(f"## Filme escolhido: **{opcao}**")
    
    imagem = Image.open(opcao)
    st.image(imagem, caption=opcao, use_column_width=True)

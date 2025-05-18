import streamlit as st
import random
from PIL import Image

st.set_page_config(page_title="Roleta de Filmes", page_icon="🎬", layout="centered")

st.title("Roleta de Filmes")
st.write("Clique no botão abaixo para rodar a roleta entre *Kung Fu Panda* e *Ratatouille*.")

if st.button("Rodar Roleta"):
    opcao = random.choice(["Kung Fu Panda", "Ratatouille"])
    st.markdown(f"## Filme escolhido: **{opcao}**")
    
    imagem_path = f"{opcao.lower().replace(' ', '_')}.jpg"
    imagem = Image.open(imagem_path)
    st.image(imagem, caption=opcao, use_column_width=True)

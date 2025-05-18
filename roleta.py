import streamlit as st
import random
import requests
from PIL import Image
from io import BytesIO

# URLs das imagens
URLS = {
    "Kung Fu Panda": "https://upload.wikimedia.org/wikipedia/en/7/76/Kungfupanda.jpg",
    "Ratatouille": "https://m.media-amazon.com/images/I/81r+LN7kAfL._AC_UF894,1000_QL80_.jpg"
}

st.set_page_config(page_title="Roleta de Filmes", page_icon="🎬", layout="centered")
st.title("Roleta de Filmes")
st.write("Clique no botão abaixo para rodar a roleta entre *Kung Fu Panda* e *Ratatouille*.")

if st.button("Rodar Roleta"):
    filme = random.choice(list(URLS.keys()))
    st.markdown(f"## Filme escolhido: **{filme}**")

    # Carrega imagem da URL
    response = requests.get(URLS[filme])
    image = Image.open(BytesIO(response.content))
    
    st.image(image, caption=filme, use_column_width=True)

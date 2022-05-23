import streamlit
streamlit.title("My first streamlit app.")
from PIL import Image
image = Image.open('sunrise.jpg')

st.image(image, caption='Sunrise by the mountains')

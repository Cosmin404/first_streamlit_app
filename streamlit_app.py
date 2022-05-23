import streamlit
streamlit.title("My first streamlit app.")

image = Image.open('https://www.google.com/url?sa=i&url=https%3A%2F%2Fid.usembassy.gov%2Fstudy-on-the-peoples-republic-of-chinas-south-china-sea-maritime-claims%2F&psig=AOvVaw1OQx6FX9zEPvTc4arokrM1&ust=1653376755187000&source=images&cd=vfe&ved=0CAwQjRxqFwoTCKiz4sOK9fcCFQAAAAAdAAAAABAD')
st.image(image, caption='Sunrise by the mountains')

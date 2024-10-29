import streamlit as st

from streamlit_image_select import image_select
 
img = image_select("Select a image", ["./images/venti.png", "./images/paimeng.png", "./images/yin.png"], use_container_width=False)
st.write(img)

if img == "./images/venti.png":
    st.write("This is Venti")

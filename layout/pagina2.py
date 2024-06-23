import streamlit as st
from styles.theme import theme


def write():
    left, middle, right = st.columns(3)
    theme()
    """Usado para escribir la página en la aplicación"""
    right.title("Página 1")
    st.write("Esta es la página 1")
    #st.video("https://www.youtube.com/watch?v=3YQb-0P320s&list=RDMM&index=23")
    st.image('assets/demo_grafica.png', caption='Sunrise by the mountains')
    video_file = open('assets/demo_regression.mp4', 'rb')
    video_bytes = video_file.read()

    st.video(video_bytes, autoplay=True,loop=True,muted=True)
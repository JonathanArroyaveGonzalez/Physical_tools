import streamlit as st
from st_pages import add_page_title

st.set_page_config(
    page_title="Example ...",
    page_icon=":shark:",
)

add_page_title("Pagina Example...")

st.write("This is just a sample page!")

st.latex("\int a x^2 \, dx")
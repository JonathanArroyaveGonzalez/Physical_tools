import streamlit as st
from pages import page1
from layout import pagina2,regressions,home


PAGES = {
    "Inicio": home,
    "Calculadora de Regresiones": regressions,
    "Pagina 2": pagina2,

}

def main():
    st.set_page_config(
        page_title="Physical Tools",
        page_icon=":shark:",
    )
    st.sidebar.title("Navegación")
    choice = st.sidebar.radio("Ir a", list(PAGES.keys()))

    PAGES[choice].write()

if __name__ == "__main__":
    main()


import streamlit as st
from layout import regressions,home,ley_de_hooke


PAGES = {
    "Inicio": home,
    "Calculadora de Regresiones": regressions,
    "Simulador Ley de hooke": ley_de_hooke,

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


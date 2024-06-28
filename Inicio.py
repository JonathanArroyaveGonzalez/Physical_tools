import streamlit as st
from layout import regressions, home, ley_de_hooke, calculator_mod
from styles.theme import theme

PAGES = {
    "🚩 Inicio": home,
    "🚩 Calculadora de Regresiones": regressions,
    "🚩 Simulador Ley de Hooke": ley_de_hooke,
    "🚩 Calculadora de % de error": calculator_mod,
}


def main():
    st.set_page_config(
        page_title="Physical Tools",
        page_icon=":cyclone:",
        layout="wide",
    )
    with st.sidebar:
        theme()

    st.sidebar.title("➤ Navegación")
    choice = st.sidebar.radio("Ir a 📌", list(PAGES.keys()))
    st.sidebar.header("Acerca de ...")

    PAGES[choice].write()  # Simplified page rendering



if __name__ == "__main__":
    main()




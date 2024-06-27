import streamlit as st
from layout import regressions, home, ley_de_hooke
from styles.theme import theme

PAGES = {
    "Inicio": home,
    "Calculadora de Regresiones": regressions,
    "Simulador Ley de Hooke": ley_de_hooke,
}


def main():
    with st.sidebar:
        theme()

    st.sidebar.title("Navegación")
    choice = st.sidebar.radio("Ir a", list(PAGES.keys()))

    PAGES[choice].write()  # Simplified page rendering



if __name__ == "__main__":
    main()




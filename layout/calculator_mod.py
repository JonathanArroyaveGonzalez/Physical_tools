import streamlit as st

def write():
    st.markdown(
        """
        <style>
            .stApp {
                text-align: center; /* Centra todo el contenido de la aplicación */
            }

        </style>
        """,
        unsafe_allow_html=True,
    )
    st.title("Calculadora de Porcentaje de Error 🔢")

    st.markdown(
        "<p style='text-align: justify;'>El porcentaje de error es, formalmente, la magnitud de la diferencia entre un valor exacto y uno aproximado, dividida por la magnitud del valor exacto por 100 casos (tiene forma de porcentaje). Básicamente, esta medida te permite ver qué tan lejos está un valor aproximado de uno exacto a través de un porcentaje del valor exacto. El error puede deberse al método de medición (herramienta o error humano) o a las aproximaciones que se usan en el cálculo (por ejemplo, errores de redondeo).</p>",
        unsafe_allow_html=True)

    st.latex(r"""
    \begin{align*}
    \text{Porcentaje de Error } &= \frac{| \text{Valor Experimental} - \text{Valor Teórico} |}{\text{Valor Teórico}}\times 100\% \\
    \end{align*}
    """)
    # Entradas de usuario
    valor_experimental = st.number_input("Valor experimental:", placeholder="Ingrese el valor experimental")
    valor_teorico = st.number_input("Valor teórico:", placeholder='Ingrese el valor teorico')

    # Cálculo del error
    if valor_teorico != 0:  # Evitar división por cero
        error_absoluto = abs(valor_experimental - valor_teorico)
        porcentaje_error_absoluto = (error_absoluto / valor_teorico) * 100

        # Mostrar resultados
        st.subheader("Resultados:")
        st.title(f'Porcentaje de error: :red[{porcentaje_error_absoluto:.1f}%]')

    else:
        st.warning("El valor teórico no puede ser cero.")

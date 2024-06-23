import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import pandas as pd
from styles.theme import theme


def calcular_regresion(x, y, tipo):
    x = np.array(x).reshape((-1, 1))
    y = np.array(y)

    if tipo == 'Lineal':
        model = LinearRegression()
    else:
        poly_features = PolynomialFeatures(degree=2)
        x = poly_features.fit_transform(x)
        model = LinearRegression()

    model.fit(x, y)
    y_pred = model.predict(x)
    r2 = model.score(x, y)

    if tipo == 'Lineal':
        ecuacion = f'y = {model.coef_[0]:.2f}x + {model.intercept_:.2f}'
    else:
        ecuacion = f'y = {model.coef_[2]:.2f}x^2 + {model.coef_[1]:.2f}x + {model.coef_[0]:.2f}'

    return y_pred, r2, ecuacion


def graficar_regresion(x, y, y_pred, r2, ecuacion):
    fig, ax = plt.subplots()
    ax.scatter(x, y, color='blue', label='Datos')
    ax.plot(x, y_pred, color='red', label='Regresión')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('Regresión')
    ax.text(0.05, 0.95, f'R^2 = {r2:.2f}', transform=ax.transAxes)
    ax.text(0.05, 0.90, f'Ecuación: {ecuacion}', transform=ax.transAxes)
    ax.legend()
    st.pyplot(fig)


def write():
    st.markdown(
        """
        <style>
            .stApp {
                text-align: center; /* Centra todo el contenido de la aplicación */
            }
            .stButton button { /* Estilo específico para el botón */
                width: 200px; /* Ajusta el ancho según tus preferencias */
            }



        </style>
        """,
        unsafe_allow_html=True,
    )
    theme()
    st.title('Calculadora de Regresión')
    tipo_regresion = st.radio('Selecciona el tipo de regresión', ('Lineal', 'Cuadrática'))

    st.subheader('Ingresa los datos')

    # Tabla inicial (opcional, puedes comenzar con una tabla vacía)

    df = pd.DataFrame(columns=["Eje X", "Eje Y"])

    # Editor de datos
    edited_df = st.data_editor(df, num_rows="dynamic")

    if st.button('Calcular'):
        # Validaciones directamente desde el DataFrame editado
        if edited_df.isnull().values.any():
            st.error('Por favor, completa todos los campos de la tabla.')
        else:
            try:
                # Obtener valores de X e Y
                x = edited_df["Eje X"].astype(float).tolist()
                y = edited_df["Eje Y"].astype(float).tolist()

                if len(x) != len(y):
                    st.error('El número de datos en X y Y debe ser igual')
                else:
                    # Realizar los cálculos y gráficos
                    y_pred, r2, ecuacion = calcular_regresion(x, y, tipo_regresion)
                    graficar_regresion(x, y, y_pred, r2, ecuacion)
            except ValueError:
                st.error('Asegúrate de ingresar solo números válidos en la tabla.')

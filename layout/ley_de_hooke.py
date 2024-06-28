import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time
#from styles.theme import theme


def plot_spring_motion(k, m, time_point):
    t = np.linspace(0, 10, 400)
    omega = np.sqrt(k / m)
    x = np.sin(omega * t)

    # Crear el gráfico (una sola vez)
    fig, ax = plt.subplots()
    line, = ax.plot(t, x, label='Onda completa')  # Almacenar la línea
    point, = ax.plot([], [], 'ro', label='Posición actual')  # Punto inicial vacío
    ax.set_xlim([0, 10])
    ax.set_ylim([-1.5, 1.5])
    ax.set_xlabel('Tiempo (segundos)')
    ax.set_ylabel('Desplazamiento (metros)')
    ax.set_title('Movimiento del Resorte en el Tiempo')
    ax.legend()
    return fig, line, point

def write():
 #   theme()
    # Configuración inicial de Streamlit
    st.title('Simulación de la Ley de Hooke con Visualización Dinámica 👩🏾‍💻')
    # Sección de Teoría
    with st.expander("Teoría de la Ley de Hooke"):
        st.markdown("""
        La **Ley de Hooke** describe la relación entre la fuerza aplicada a un resorte y su deformación. En términos simples, establece que la fuerza ejercida por un resorte es directamente proporcional a la distancia que se estira o comprime desde su posición de equilibrio.

        **Fórmula:**

        ```
        F = -K * 🛆x
        ```

        Donde:

        * F es la fuerza (en Newton).
        * k es la constante elástica del resorte (en N/m), una medida de su rigidez.
        * 🛆x es la variación que experimenta la longitud del resorte, ya sea una compresión o extensión.

        **Movimiento Armónico Simple (MAS):**

        Un sistema masa-resorte ideal, donde la única fuerza actuante es la del resorte, exhibe un movimiento armónico simple (MAS). En este tipo de movimiento, la posición de la masa en función del tiempo se describe mediante una función sinusoidal.

        **Fórmulas Adicionales:**

        ```
        ω = √(k/m)  (Frecuencia angular)
        T = 2π/ω   (Periodo)
        f = 1/T     (Frecuencia)
        ```
        """)

    k = st.slider('Constante elástica k (N/m)', 1.0, 100.0, 20.0, 0.5)
    m = st.slider('Masa suspendida m (kg)', 0.1, 10.0, 1.0, 0.1)

    # Crear el gráfico solo una vez
    fig, line, point = plot_spring_motion(k, m, 0)  # Gráfico inicial
    plot_placeholder = st.pyplot(fig)  # Placeholder para actualizar el gráfico

    # Botones para controlar la animación
    if 'running' not in st.session_state:
        st.session_state.running = False
    start_button = st.button('Iniciar Simulación')
    stop_button = st.button('Terminar Simulación')

    if start_button:
        st.session_state.running = True
    if stop_button:
        st.session_state.running = False

    # Animación
    if st.session_state.running:
        try:
            for time_point in np.arange(0, 100, 0.05):  # Rango extendido
                line.set_ydata(np.sin(np.sqrt(k / m) * line.get_xdata()))
                point.set_data([time_point % 10], [np.sin(np.sqrt(k / m) * (time_point % 10))])
                plot_placeholder.pyplot(fig)
                time.sleep(0.05)
                if not st.session_state.running:
                    break
        except Exception as e:
            st.exception(e)
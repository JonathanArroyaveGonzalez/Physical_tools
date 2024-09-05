import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time


def plot_spring_motion(k, m):
    t = np.linspace(0, 10, 400)
    omega = np.sqrt(k / m)
    x = np.sin(omega * t)

    fig, ax = plt.subplots()
    line, = ax.plot(t, x, label='Onda completa')
    point, = ax.plot([], [], 'ro', label='Posición actual')

    ax.set_xlim([0, 10])
    ax.set_ylim([-1.5, 1.5])
    ax.set_xlabel('Tiempo (segundos)')
    ax.set_ylabel('Desplazamiento (metros)')
    ax.set_title('Movimiento del Resorte en el Tiempo')
    ax.legend()

    return fig, line, point, t


def update_plot(line, point, t, omega, frame):
    y_data = np.sin(omega * t)
    line.set_ydata(y_data)
    point.set_data([t[frame]], [y_data[frame]])


def write():
    st.title('Simulación de la Ley de Hooke con Visualización Dinámica 👩🏾‍💻')

    # Sección de Teoría
    with st.expander("Teoría de la Ley de Hooke"):
        st.markdown("""
        La **Ley de Hooke** describe la relación entre la fuerza aplicada a un resorte y su deformación. En términos simples, establece que la fuerza ejercida por un resorte es directamente proporcional a la distancia que se estira o comprime desde su posición de equilibrio.

        **Fórmula:**
        ```
        F = -K * Δx
        ```
        Donde:
        * F es la fuerza (en Newton).
        * k es la constante elástica del resorte (en N/m), una medida de su rigidez.
        * Δx es la variación que experimenta la longitud del resorte, ya sea una compresión o extensión.
        """)

    # Parámetros ajustables
    k = st.slider('Constante elástica k (N/m)', 1.0, 100.0, 20.0, 0.5)
    m = st.slider('Masa suspendida m (kg)', 0.1, 10.0, 1.0, 0.1)

    # Crear el gráfico una vez
    fig, line, point, t = plot_spring_motion(k, m)
    plot_placeholder = st.pyplot(fig)

    # Botones para controlar la animación
    if 'running' not in st.session_state:
        st.session_state.running = False
    start_button = st.button('Iniciar Simulación')
    stop_button = st.button('Terminar Simulación')

    if start_button:
        st.session_state.running = True
    if stop_button:
        st.session_state.running = False

    omega = np.sqrt(k / m)
    frames = len(t)

    if st.session_state.running:
        for frame in range(frames):
            if not st.session_state.running:
                break
            update_plot(line, point, t, omega, frame)
            plot_placeholder.pyplot(fig)
            time.sleep(0.05)





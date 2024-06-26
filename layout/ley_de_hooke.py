import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time

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
    # Configuración inicial de Streamlit
    st.title('Simulación de la Ley de Hooke con Visualización Dinámica')
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
            for time_point in np.arange(0, 10, 0.05):  # Pasos más pequeños para mayor fluidez
                line.set_ydata(np.sin(np.sqrt(k / m) * line.get_xdata()))
                point.set_data([time_point], [np.sin(np.sqrt(k / m) * time_point)])
                plot_placeholder.pyplot(fig)  # Actualizar el gráfico existente
                time.sleep(0.05)
                if not st.session_state.running:
                    break
        except Exception as e:
            st.exception(e)

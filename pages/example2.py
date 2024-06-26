import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import tempfile

# Configuración de la página
st.set_page_config(page_title="Simulación de la Ley de Hooke")

# Título y descripción
st.title("Simulación de la Ley de Hooke")
st.write("Explora el comportamiento de un sistema masa-resorte ajustando los parámetros.")

# Barra lateral para la entrada de parámetros
st.sidebar.header("Parámetros")
mass = st.sidebar.slider("Masa (m) en kg", 0.1, 10.0, 1.0, 0.1)
spring_constant = st.sidebar.slider("Constante del resorte (k) en N/m", 1.0, 100.0, 10.0, 0.1)
amplitude = st.sidebar.slider("Amplitud (A) en m", 0.1, 2.0, 1.0, 0.1)

# Calcular la frecuencia angular
angular_frequency = np.sqrt(spring_constant / mass)

# Arreglo de tiempo
t = np.linspace(0, 10, 1000)


# Función de posición
def position(t):
    return amplitude * np.cos(angular_frequency * t)


# Crear figura y ejes
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
plt.close()

# Visualización del sistema masa-resorte
line, = ax1.plot([], [], 'bo-', lw=2)
spring, = ax1.plot([], [], 'r-', lw=1)
ax1.set_xlim(-2, 2)
ax1.set_ylim(-2, 2)
ax1.set_aspect('equal', adjustable='box')
ax1.set_title("Sistema Masa-Resorte")
ax1.set_xlabel("Posición (m)")
ax1.set_ylabel("Altura (m)")

# Visualización de la onda sinusoidal
wave, = ax2.plot([], [], 'b-', lw=2)
ax2.set_xlim(0, 10)
ax2.set_ylim(-2, 2)
ax2.set_title("Desplazamiento vs Tiempo")
ax2.set_xlabel("Tiempo (s)")
ax2.set_ylabel("Desplazamiento (m)")


# Función de animación
def animate(frame):
    t = frame / 50
    x = position(t)

    # Actualizar el sistema masa-resorte
    line.set_data([0, x], [0, 0])
    spring_x = np.linspace(0, x, 50)
    spring_y = 0.1 * np.sin(50 * spring_x)
    spring.set_data(spring_x, spring_y)

    # Actualizar la onda sinusoidal
    wave.set_data(np.linspace(0, t, 100), position(np.linspace(0, t, 100)))

    return line, spring, wave


# Crear la animación
anim = FuncAnimation(fig, animate, frames=500, interval=20, blit=True)

# Guardar la animación en un archivo temporal
with tempfile.NamedTemporaryFile(delete=False, suffix=".gif") as tmpfile:
    anim.save(tmpfile.name, writer='pillow', fps=30)
    tmpfile.seek(0)
    gif_path = tmpfile.name

# Mostrar la animación en Streamlit
st.image(gif_path)

# Mostrar ecuaciones y explicaciones
st.header("Ecuaciones y Explicaciones")
st.latex(r"F = -kx \quad \text{(Ley de Hooke)}")
st.latex(r"\omega = \sqrt{\frac{k}{m}} \quad \text{(Frecuencia Angular)}")
st.latex(r"x(t) = A \cos(\omega t) \quad \text{(Posición en función del tiempo)}")

st.write("""
En esta simulación:
- El gráfico superior muestra el sistema masa-resorte oscilando.
- El gráfico inferior muestra el desplazamiento de la masa a lo largo del tiempo, formando una onda sinusoidal.
- A medida que ajustas los parámetros, observa cómo afectan el movimiento del sistema:
  - Aumentar la masa (m) disminuye la frecuencia de oscilación.
  - Aumentar la constante del resorte (k) incrementa la frecuencia de oscilación.
  - Cambiar la amplitud (A) afecta el desplazamiento máximo de la masa.
""")

# Mostrar valores actuales de los parámetros
st.header("Valores Actuales de los Parámetros")
st.write(f"Masa (m): {mass} kg")
st.write(f"Constante del resorte (k): {spring_constant} N/m")
st.write(f"Amplitud (A): {amplitude} m")
st.write(f"Frecuencia Angular (ω): {angular_frequency:.2f} rad/s")
st.write(f"Frecuencia (f): {angular_frequency / (2 * np.pi):.2f} Hz")
st.write(f"Periodo (T): {2 * np.pi / angular_frequency:.2f} s")

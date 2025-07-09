import streamlit as st
import numpy as np
import plotly.graph_objects as go
from utils.ui_components import create_plotly_figure

st.set_page_config(page_title="Ecuación de la Recta", page_icon="📐", layout="wide")

st.title("Graficador de la Ecuación de la Recta")
st.write("Introduce la pendiente (m) y el intercepto en y (b) para calcular y visualizar la recta `y = mx + b`.")

# --- Boton para volver al menú principal ---
st.page_link("app.py", label="← Volver al Menú Principal", icon="🏠")
st.markdown("---")

# --- Entradas de Usuario ---
st.subheader("Parámetros de la Recta")
st.write("Mueve los sliders para ver cómo cambia la recta en tiempo real.")
col1, col2 = st.columns(2)
with col1:
    m = st.slider("Pendiente (m)", min_value=-10.0, max_value=10.0, value=1.0, step=0.1)
with col2:
    b = st.slider("Intercepto en y (b)", min_value=-10.0, max_value=10.0, value=2.0, step=0.1)

# --- Ecuación y Gráfica (se actualizan en tiempo real) ---
st.markdown("---")
st.subheader("Ecuación Resultante")

# Formateo para mostrar el signo de 'b' correctamente
signo = "+" if b >= 0 else "-"
b_abs = abs(b)
ecuacion_final_str = f"y = {m:.2f}x {signo} {b_abs:.2f}"
st.latex(ecuacion_final_str)
st.metric(label="Ecuación de la Recta", value=ecuacion_final_str)

st.markdown("---")
st.subheader("Visualización Gráfica")

# --- Preparación de datos para la Gráfica ---
traces = []
annotations = []

# 1. Definir un rango para el eje x y calcular y
x_range = np.linspace(-10, 10, 400)
y_range = m * x_range + b
traces.append(go.Scatter(x=x_range, y=y_range, mode='lines', name='Recta', line=dict(color='royalblue', width=3)))

# 2. Marcar el intercepto en y
traces.append(go.Scatter(x=[0], y=[b], mode='markers+text', name='Intercepto en y',
                         marker=dict(color='crimson', size=10, symbol='circle'),
                         text=[f'b = (0, {b:.2f})'], textposition="top right"))

# 3. Anotación para la pendiente
annotations.append(dict(x=2, y=m * 2 + b, text=f"<b>m = {m:.2f}</b>", showarrow=False, yshift=15,
                         font=dict(family="Arial, sans-serif", size=14, color="purple"),
                         bgcolor="rgba(255, 255, 255, 0.7)"))

# 4. Crear y mostrar la figura
fig = create_plotly_figure(
    traces=traces,
    title=f"Gráfica de ${ecuacion_final_str}$",
    annotations=annotations
)
fig.update_layout(xaxis_range=[-10, 10], yaxis_range=[-10, 10])

st.plotly_chart(fig, use_container_width=True)

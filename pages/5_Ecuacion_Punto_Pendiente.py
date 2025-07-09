import streamlit as st
import numpy as np
import plotly.graph_objects as go
from utils.ui_components import create_plotly_figure

st.set_page_config(page_title="Ecuación de la Recta (Punto-Pendiente)", page_icon="📐", layout="wide")

st.title("Calcular Ecuación de la Recta (Punto-Pendiente)")
st.write("Introduce las coordenadas de un punto (P₁) y el valor de la pendiente (m) para encontrar la ecuación de la recta y visualizarla.")

# --- Boton para volver al menú principal ---
st.page_link("app.py", label="← Volver al Menú Principal", icon="🏠")
st.markdown("---")

# --- Entradas de Usuario ---
st.subheader("1. Datos de Entrada")
col1, col2, col3 = st.columns(3)
with col1:
    x1 = st.number_input("Coordenada x₁ del punto", value=2.0, format="%.2f", key="psp_x1")
with col2:
    y1 = st.number_input("Coordenada y₁ del punto", value=3.0, format="%.2f", key="psp_y1")
with col3:
    m = st.number_input("Valor de la pendiente (m)", value=1.5, format="%.2f", key="psp_m")

# --- Cálculo y Visualización ---
if st.button("Calcular Ecuación y Graficar"):
    st.markdown("---")
    st.subheader("2. Resultados del Cálculo")

    # --- PASO 1: FÓRMULA PUNTO-PENDIENTE ---
    st.markdown("#### Paso 1: Usar la forma Punto-Pendiente")
    st.write("Partimos de la fórmula punto-pendiente:")
    st.latex(r"y - y_1 = m(x - x_1)")
    st.write(f"Sustituimos los valores del punto P₁({x1}, {y1}) y la pendiente m={m}:")
    st.latex(fr"y - ({y1:.2f}) = {m:.2f}(x - ({x1:.2f}))")

    # --- PASO 2: CALCULAR INTERCEPTO (b) ---
    st.markdown("#### Paso 2: Despejar para la forma Pendiente-Intercepto (y = mx + b)")
    st.write("Desarrollamos la ecuación:")
    st.latex(fr"y - {y1:.2f} = {m:.2f}x - {m*x1:.2f}")
    st.write("Y despejamos 'y' para encontrar el intercepto 'b':")
    b = y1 - m * x1
    st.latex(fr"y = {m:.2f}x - {m*x1:.2f} + {y1:.2f}")
    st.latex(fr"y = {m:.2f}x + ({b:.2f})")

    # --- RESULTADO FINAL ---
    st.markdown("#### Ecuación Final")
    st.success(f"La ecuación de la recta es: **y = {m:.2f}x + {b:.2f}**")
    st.metric(label="Ecuación", value=f"y = {m:.2f}x + {b:.2f}")

    # --- GRÁFICA ---
    st.markdown("---")
    st.subheader("3. Visualización Gráfica")

    traces = []

    # 1. Dibujar la recta
    x_vals = np.array([x1 - 5, x1 + 5])
    y_vals = m * x_vals + b
    traces.append(go.Scatter(x=x_vals, y=y_vals, mode='lines', name=f'y={m:.2f}x+{b:.2f}'))

    # 2. Marcar el punto P1
    traces.append(go.Scatter(
        x=[x1], y=[y1],
        mode='markers+text', name='Punto P₁',
        marker=dict(color='crimson', size=12),
        text=[f'P₁({x1:.2f}, {y1:.2f})'],
        textposition="bottom right"
    ))

    # 3. Crear y mostrar la figura
    fig = create_plotly_figure(
        traces=traces,
        title=f"Recta que pasa por ({x1:.2f}, {y1:.2f}) con pendiente m={m:.2f}"
    )
    st.plotly_chart(fig, use_container_width=True)

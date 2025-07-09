import streamlit as st
import numpy as np
import plotly.graph_objects as go

st.set_page_config(page_title="Ecuación de la Parábola", page_icon="📐", layout="wide")

st.title("Calculadora de la Ecuación de la Parábola")
st.write("Introduce el vértice (h, k), la distancia focal (p) y la orientación para encontrar la ecuación.")

# --- Boton para volver al menú principal ---
st.page_link("app.py", label="← Volver al Menú Principal", icon="🏠")
st.markdown("---")
st.write("Aquí encontrarás un resumen de las fórmulas y conceptos clave utilizados en esta aplicación.")

# --- Entradas de Usuario ---
col1, col2, col3, col4 = st.columns(4)
with col1:
    h = st.number_input("Coordenada h del vértice", value=1.0, format="%.2f")
with col2:
    k = st.number_input("Coordenada k del vértice", value=2.0, format="%.2f")
with col3:
    p = st.number_input("Distancia focal (p)", value=2.0, min_value=0.1, format="%.2f")
with col4:
    orientation = st.selectbox("Orientación", ["Vertical (abre hacia arriba/abajo)", "Horizontal (abre hacia der/izq)"])

# --- Cálculo y Visualización ---
if st.button("Calcular Ecuación y Graficar"):
    st.markdown("---")
    st.subheader("Resultados del Cálculo")

    st.markdown("#### 1. Ecuación Estándar (Ordinaria)")
    
    if "Vertical" in orientation:
        st.write("La fórmula para una parábola vertical es:")
        st.latex(r"(x - h)^2 = 4p(y - k)")
        h_sign = "-" if h >= 0 else "+"
        h_abs = abs(h)
        k_sign = "-" if k >= 0 else "+"
        k_abs = abs(k)
        standard_eq_str = f"(x {h_sign} {h_abs:.2f})^2 = {4*p:.2f}(y {k_sign} {k_abs:.2f})"
        focus = (h, k + p)
        directrix_eq = f"y = {k - p:.2f}"
        directrix_val = k - p
    else: # Horizontal
        st.write("La fórmula para una parábola horizontal es:")
        st.latex(r"(y - k)^2 = 4p(x - h)")
        h_sign = "-" if h >= 0 else "+"
        h_abs = abs(h)
        k_sign = "-" if k >= 0 else "+"
        k_abs = abs(k)
        standard_eq_str = f"(y {k_sign} {k_abs:.2f})^2 = {4*p:.2f}(x {h_sign} {h_abs:.2f})"
        focus = (h + p, k)
        directrix_eq = f"x = {h - p:.2f}"
        directrix_val = h - p

    st.write("Sustituyendo los valores:")
    st.latex(standard_eq_str)
    st.success(f"La ecuación estándar es: **${standard_eq_str}$**")

    st.markdown("#### 2. Elementos de la Parábola")
    st.write(f"- **Vértice:** $V({h:.2f}, {k:.2f})$")
    st.write(f"- **Foco:** $F({focus[0]:.2f}, {focus[1]:.2f})$")
    st.write(f"- **Directriz:** ${directrix_eq}$")

    # --- Gráfica con Plotly ---
    st.subheader("Visualización Gráfica")
    fig = go.Figure()

    # 1. Dibujar la parábola
    if "Vertical" in orientation:
        y_range = np.linspace(k - 4*abs(p), k + 4*abs(p), 400)
        x_values = h + np.sqrt(4 * p * (y_range - k))
        # Necesitamos manejar el caso p<0 y las dos ramas
        x_parabola = h + np.sign(p) * np.sqrt(abs(4 * p * (y_range - k)))
        fig.add_trace(go.Scatter(x=x_parabola, y=y_range, mode='lines', name='Parábola'))
        # Dibujar la directriz
        x_line = np.linspace(h - 4*abs(p), h + 4*abs(p), 2)
        fig.add_trace(go.Scatter(x=x_line, y=[directrix_val, directrix_val], mode='lines', name='Directriz', line=dict(dash='dash', color='red')))
    else: # Horizontal
        x_range = np.linspace(h - 4*abs(p), h + 4*abs(p), 400)
        y_parabola = k + np.sign(p) * np.sqrt(abs(4 * p * (x_range - h)))
        fig.add_trace(go.Scatter(x=x_range, y=y_parabola, mode='lines', name='Parábola'))
        # Dibujar la directriz
        y_line = np.linspace(k - 4*abs(p), k + 4*abs(p), 2)
        fig.add_trace(go.Scatter(x=[directrix_val, directrix_val], y=y_line, mode='lines', name='Directriz', line=dict(dash='dash', color='red')))

    # 2. Marcar Vértice y Foco
    fig.add_trace(go.Scatter(x=[h], y=[k], mode='markers+text', name='Vértice', marker=dict(color='crimson', size=12), text=['Vértice'], textposition="bottom right"))
    fig.add_trace(go.Scatter(x=[focus[0]], y=[focus[1]], mode='markers+text', name='Foco', marker=dict(color='purple', size=12), text=['Foco'], textposition="top left"))

    # 3. Configurar el diseño
    fig.update_layout(
        title="Gráfica de la Parábola",
        xaxis_title="Eje X", yaxis_title="Eje Y",
        xaxis=dict(scaleanchor="y", scaleratio=1),
        yaxis=dict(scaleanchor="x", scaleratio=1),
        legend=dict(yanchor="top", y=0.99, xanchor="left", x=0.01)
    )
    fig.update_xaxes(zeroline=True, zerolinewidth=2, zerolinecolor='LightGrey')
    fig.update_yaxes(zeroline=True, zerolinewidth=2, zerolinecolor='LightGrey')

    st.plotly_chart(fig, use_container_width=True)


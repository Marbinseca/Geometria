import streamlit as st
import numpy as np
import plotly.graph_objects as go
import math

st.set_page_config(page_title="Ecuación de la Hipérbola", page_icon="📐", layout="wide")

st.title("Calculadora de la Ecuación de la Hipérbola")
st.write("Introduce el centro (h, k), los semiejes (a, b) y la orientación para encontrar la ecuación.")

# --- Boton para volver al menú principal ---
st.page_link("app.py", label="← Volver al Menú Principal", icon="🏠")
st.markdown("---")
st.write("Aquí encontrarás un resumen de las fórmulas y conceptos clave utilizados en esta aplicación.")

# --- Entradas de Usuario ---
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    h = st.number_input("Coordenada h del centro", value=0.0, format="%.2f")
with col2:
    k = st.number_input("Coordenada k del centro", value=0.0, format="%.2f")
with col3:
    a = st.number_input("Semieje transverso (a)", value=3.0, min_value=0.1, format="%.2f")
with col4:
    b = st.number_input("Semieje conjugado (b)", value=2.0, min_value=0.1, format="%.2f")
with col5:
    orientation = st.selectbox("Orientación", ["Horizontal (abre a los lados)", "Vertical (abre arriba/abajo)"])

# --- Cálculo y Visualización ---
if st.button("Calcular Ecuación y Graficar"):
    st.markdown("---")
    st.subheader("Resultados del Cálculo")

    st.markdown("#### 1. Ecuación Estándar (Ordinaria)")
    h_sign = "-" if h >= 0 else "+"
    h_abs = abs(h)
    k_sign = "-" if k >= 0 else "+"
    k_abs = abs(k)

    if "Horizontal" in orientation:
        st.write("La fórmula para una hipérbola horizontal es:")
        st.latex(r"\frac{(x - h)^2}{a^2} - \frac{(y - k)^2}{b^2} = 1")
        standard_eq_str = f"\\frac{{(x {h_sign} {h_abs:.2f})^2}}{{{a**2:.2f}}} - \\frac{{(y {k_sign} {k_abs:.2f})^2}}{{{b**2:.2f}}} = 1"
    else: # Vertical
        st.write("La fórmula para una hipérbola vertical es:")
        st.latex(r"\frac{(y - k)^2}{a^2} - \frac{(x - h)^2}{b^2} = 1")
        standard_eq_str = f"\\frac{{(y {k_sign} {k_abs:.2f})^2}}{{{a**2:.2f}}} - \\frac{{(x {h_sign} {h_abs:.2f})^2}}{{{b**2:.2f}}} = 1"

    st.write("Sustituyendo los valores:")
    st.latex(standard_eq_str)
    st.success(f"La ecuación estándar es: **${standard_eq_str}$**")

    st.markdown("#### 2. Elementos de la Hipérbola")
    c = math.sqrt(a**2 + b**2)
    st.write(f"- **Centro:** $C({h:.2f}, {k:.2f})$")
    if "Horizontal" in orientation:
        st.write(f"- **Vértices:** $({h-a:.2f}, {k:.2f})$ y $({h+a:.2f}, {k:.2f})$")
        st.write(f"- **Focos:** $({h-c:.2f}, {k:.2f})$ y $({h+c:.2f}, {k:.2f})$")
        st.write(f"- **Asíntotas:** $y - {k:.2f} = \\pm \\frac{{{b:.2f}}}{{{a:.2f}}}(x - {h:.2f})$")
    else: # Vertical
        st.write(f"- **Vértices:** $({h:.2f}, {k-a:.2f})$ y $({h:.2f}, {k+a:.2f})$")
        st.write(f"- **Focos:** $({h:.2f}, {k-c:.2f})$ y $({h:.2f}, {k+c:.2f})$")
        st.write(f"- **Asíntotas:** $y - {k:.2f} = \\pm \\frac{{{a:.2f}}}{{{b:.2f}}}(x - {h:.2f})$")

    # --- Gráfica con Plotly ---
    st.subheader("Visualización Gráfica")
    fig = go.Figure()

    # 1. Dibujar la hipérbola
    if "Horizontal" in orientation:
        x_range = np.linspace(h - 4*a, h + 4*a, 400)
        y_hyperbola_pos = k + b * np.sqrt(np.maximum(0, ((x_range - h)**2 / a**2) - 1))
        y_hyperbola_neg = k - b * np.sqrt(np.maximum(0, ((x_range - h)**2 / a**2) - 1))
        fig.add_trace(go.Scatter(x=x_range, y=y_hyperbola_pos, mode='lines', name='Hipérbola', line_color='royalblue'))
        fig.add_trace(go.Scatter(x=x_range, y=y_hyperbola_neg, mode='lines', showlegend=False, line_color='royalblue'))
        # Asíntotas
        x_asym = np.array([h - 4*a, h + 4*a])
        y_asym1 = (b/a)*(x_asym - h) + k
        y_asym2 = -(b/a)*(x_asym - h) + k
    else: # Vertical
        y_range = np.linspace(k - 4*a, k + 4*a, 400)
        x_hyperbola_pos = h + b * np.sqrt(np.maximum(0, ((y_range - k)**2 / a**2) - 1))
        x_hyperbola_neg = h - b * np.sqrt(np.maximum(0, ((y_range - k)**2 / a**2) - 1))
        fig.add_trace(go.Scatter(x=x_hyperbola_pos, y=y_range, mode='lines', name='Hipérbola', line_color='royalblue'))
        fig.add_trace(go.Scatter(x=x_hyperbola_neg, y=y_range, mode='lines', showlegend=False, line_color='royalblue'))
        # Asíntotas
        x_asym = np.array([h - 4*b, h + 4*b])
        y_asym1 = (a/b)*(x_asym - h) + k
        y_asym2 = -(a/b)*(x_asym - h) + k

    fig.add_trace(go.Scatter(x=x_asym, y=y_asym1, mode='lines', name='Asíntotas', line=dict(dash='dash', color='red')))
    fig.add_trace(go.Scatter(x=x_asym, y=y_asym2, mode='lines', showlegend=False, line=dict(dash='dash', color='red')))

    # 2. Marcar el centro
    fig.add_trace(go.Scatter(x=[h], y=[k], mode='markers', name='Centro', marker=dict(color='crimson', size=12)))

    # 3. Configurar el diseño
    fig.update_layout(
        title="Gráfica de la Hipérbola",
        xaxis_title="Eje X", yaxis_title="Eje Y",
        xaxis=dict(scaleanchor="y", scaleratio=1),
        yaxis=dict(scaleanchor="x", scaleratio=1),
        legend=dict(yanchor="top", y=0.99, xanchor="left", x=0.01)
    )
    fig.update_xaxes(zeroline=True, zerolinewidth=2, zerolinecolor='LightGrey')
    fig.update_yaxes(zeroline=True, zerolinewidth=2, zerolinecolor='LightGrey')

    st.plotly_chart(fig, use_container_width=True)
    
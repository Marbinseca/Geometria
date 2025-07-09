import streamlit as st
import numpy as np
import plotly.graph_objects as go
import math

st.set_page_config(page_title="Ecuación de la Elipse", page_icon="📐", layout="wide")

st.title("Calculadora de la Ecuación de la Elipse")
st.write("Introduce el centro (h, k) y los semiejes (a, b) para encontrar la ecuación.")

# --- Boton para volver al menú principal ---
st.page_link("app.py", label="← Volver al Menú Principal", icon="🏠")
st.markdown("---")
st.write("Aquí encontrarás un resumen de las fórmulas y conceptos clave utilizados en esta aplicación.")

# --- Entradas de Usuario ---
col1, col2, col3, col4 = st.columns(4)
with col1:
    h = st.number_input("Coordenada h del centro", value=0.0, format="%.2f")
with col2:
    k = st.number_input("Coordenada k del centro", value=0.0, format="%.2f")
with col3:
    a = st.number_input("Semieje horizontal (a)", value=5.0, min_value=0.1, format="%.2f")
with col4:
    b = st.number_input("Semieje vertical (b)", value=3.0, min_value=0.1, format="%.2f")

# --- Cálculo y Visualización ---
if st.button("Calcular Ecuación y Graficar"):
    st.markdown("---")
    st.subheader("Resultados del Cálculo")

    st.markdown("#### 1. Ecuación Estándar (Ordinaria)")
    st.write("La fórmula estándar de la elipse es:")
    st.latex(r"\frac{(x - h)^2}{a^2} + \frac{(y - k)^2}{b^2} = 1")

    h_sign = "-" if h >= 0 else "+"
    h_abs = abs(h)
    k_sign = "-" if k >= 0 else "+"
    k_abs = abs(k)
    
    standard_eq_str = f"\\frac{{(x {h_sign} {h_abs:.2f})^2}}{{{a**2:.2f}}} + \\frac{{(y {k_sign} {k_abs:.2f})^2}}{{{b**2:.2f}}} = 1"
    st.write("Sustituyendo los valores:")
    st.latex(standard_eq_str)
    st.success(f"La ecuación estándar es: **${standard_eq_str}$**")

    st.markdown("#### 2. Elementos de la Elipse")
    st.write(f"- **Centro:** $C({h:.2f}, {k:.2f})$")
    st.write(f"- **Vértices Horizontales:** $({h-a:.2f}, {k:.2f})$ y $({h+a:.2f}, {k:.2f})$")
    st.write(f"- **Vértices Verticales:** $({h:.2f}, {k-b:.2f})$ y $({h:.2f}, {k+b:.2f})$")

    # Cálculo de los focos
    if a > b:
        c = math.sqrt(a**2 - b**2)
        foci = [(h-c, k), (h+c, k)]
        st.write(f"- **Focos:** $F_1({foci[0][0]:.2f}, {foci[0][1]:.2f})$ y $F_2({foci[1][0]:.2f}, {foci[1][1]:.2f})$")
    elif b > a:
        c = math.sqrt(b**2 - a**2)
        foci = [(h, k-c), (h, k+c)]
        st.write(f"- **Focos:** $F_1({foci[0][0]:.2f}, {foci[0][1]:.2f})$ y $F_2({foci[1][0]:.2f}, {foci[1][1]:.2f})$")
    else: # Es una circunferencia
        c = 0
        foci = [(h,k)]
        st.write("- **Focos:** Coinciden con el centro.")

    # --- Gráfica con Plotly ---
    st.subheader("Visualización Gráfica")
    fig = go.Figure()

    # 1. Dibujar la elipse
    theta = np.linspace(0, 2 * np.pi, 100)
    x_ellipse = h + a * np.cos(theta)
    y_ellipse = k + b * np.sin(theta)
    fig.add_trace(go.Scatter(x=x_ellipse, y=y_ellipse, mode='lines', name='Elipse', line=dict(color='royalblue', width=3)))

    # 2. Marcar el centro y los focos
    fig.add_trace(go.Scatter(x=[h], y=[k], mode='markers+text', name='Centro', marker=dict(color='crimson', size=12), text=['Centro'], textposition="top center"))
    
    foci_x = [f[0] for f in foci]
    foci_y = [f[1] for f in foci]
    foci_text = [f'F{i+1}' for i in range(len(foci))]
    fig.add_trace(go.Scatter(x=foci_x, y=foci_y, mode='markers+text', name='Focos', marker=dict(color='purple', size=10), text=foci_text, textposition="bottom center"))

    # 3. Configurar el diseño
    fig.update_layout(
        title="Gráfica de la Elipse",
        xaxis_title="Eje X", yaxis_title="Eje Y",
        xaxis=dict(scaleanchor="y", scaleratio=1),
        yaxis=dict(scaleanchor="x", scaleratio=1),
        legend=dict(yanchor="top", y=0.99, xanchor="left", x=0.01)
    )
    fig.update_xaxes(zeroline=True, zerolinewidth=2, zerolinecolor='LightGrey')
    fig.update_yaxes(zeroline=True, zerolinewidth=2, zerolinecolor='LightGrey')

    st.plotly_chart(fig, use_container_width=True)


import streamlit as st
import numpy as np
import plotly.graph_objects as go

st.set_page_config(page_title="Ecuación de la Circunferencia", page_icon="📐", layout="wide")

st.title("Calculadora de la Ecuación de la Circunferencia")
st.write("Introduce las coordenadas del centro (h, k) y el valor del radio (r) para encontrar la ecuación de la circunferencia.")

# --- Boton para volver al menú principal ---
st.page_link("app.py", label="← Volver al Menú Principal", icon="🏠")
st.markdown("---")
st.write("Aquí encontrarás un resumen de las fórmulas y conceptos clave utilizados en esta aplicación.")

# --- Entradas de Usuario ---
col1, col2, col3 = st.columns(3)
with col1:
    h = st.number_input("Coordenada h del centro", value=2.0, format="%.2f")
with col2:
    k = st.number_input("Coordenada k del centro", value=3.0, format="%.2f")
with col3:
    r = st.number_input("Valor del radio (r)", value=5.0, min_value=0.1, format="%.2f")

# --- Cálculo y Visualización ---
if st.button("Calcular Ecuación y Graficar"):
    st.markdown("---")
    st.subheader("Resultados del Cálculo")

    # --- Ecuación Estándar (Ordinaria) ---
    st.markdown("#### 1. Ecuación Estándar (Ordinaria)")
    st.write("Partimos de la fórmula estándar:")
    st.latex(r"(x - h)^2 + (y - k)^2 = r^2")
    
    st.write(f"Sustituimos los valores del centro C({h}, {k}) y el radio r={r}:")
    # Formateo para signos
    h_sign = "-" if h >= 0 else "+"
    h_abs = abs(h)
    k_sign = "-" if k >= 0 else "+"
    k_abs = abs(k)
    
    standard_eq_str = f"(x {h_sign} {h_abs:.2f})^2 + (y {k_sign} {k_abs:.2f})^2 = {r**2:.2f}"
    st.latex(standard_eq_str)
    st.success(f"La ecuación estándar es: **${standard_eq_str}$**")

    # --- Ecuación General ---
    st.markdown("#### 2. Ecuación General")
    st.write("Para encontrar la ecuación general `x² + y² + Dx + Ey + F = 0`, expandimos la ecuación estándar.")
    D = -2 * h
    E = -2 * k
    F = h**2 + k**2 - r**2
    
    # Formateo para signos
    D_sign = "+" if D >= 0 else "-"
    D_abs = abs(D)
    E_sign = "+" if E >= 0 else "-"
    E_abs = abs(E)
    F_sign = "+" if F >= 0 else "-"
    F_abs = abs(F)

    general_eq_str = f"x^2 + y^2 {D_sign} {D_abs:.2f}x {E_sign} {E_abs:.2f}y {F_sign} {F_abs:.2f} = 0"
    st.latex(general_eq_str)
    st.success(f"La ecuación general es: **${general_eq_str}$**")

    # --- Gráfica con Plotly ---
    st.subheader("Visualización Gráfica")
    fig = go.Figure()

    # 1. Dibujar la circunferencia
    theta = np.linspace(0, 2 * np.pi, 100)
    x_circle = h + r * np.cos(theta)
    y_circle = k + r * np.sin(theta)
    fig.add_trace(go.Scatter(x=x_circle, y=y_circle, mode='lines', name='Circunferencia', line=dict(color='royalblue', width=3)))

    # 2. Marcar el centro
    fig.add_trace(go.Scatter(
        x=[h], y=[k], mode='markers+text', name='Centro',
        marker=dict(color='crimson', size=12),
        text=[f'C({h:.2f}, {k:.2f})'], textposition="top right"
    ))

    # 3. Dibujar el radio
    fig.add_trace(go.Scatter(
        x=[h, h + r], y=[k, k], mode='lines+text', name='Radio',
        line=dict(color='green', dash='dash'),
        text=['', f'r={r:.2f}'], textposition="middle right"
    ))

    # 4. Configurar el diseño de la gráfica
    fig.update_layout(
        title="Gráfica de la Circunferencia",
        xaxis_title="Eje X", yaxis_title="Eje Y",
        xaxis=dict(scaleanchor="y", scaleratio=1),
        yaxis=dict(scaleanchor="x", scaleratio=1),
        legend=dict(yanchor="top", y=0.99, xanchor="left", x=0.01)
    )
    fig.update_xaxes(zeroline=True, zerolinewidth=2, zerolinecolor='LightGrey')
    fig.update_yaxes(zeroline=True, zerolinewidth=2, zerolinecolor='LightGrey')

    st.plotly_chart(fig, use_container_width=True)


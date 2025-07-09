import streamlit as st
import numpy as np
import plotly.graph_objects as go
from utils.ui_components import create_plotly_figure

st.set_page_config(page_title="Coordenadas Polares", page_icon="🧭", layout="wide")

st.title("Conversor de Coordenadas Polares y Cartesianas")
st.write("Utiliza esta herramienta para convertir coordenadas entre el sistema cartesiano (x, y) y el sistema polar (r, θ).")

# --- Boton para volver al menú principal ---
st.page_link("app.py", label="← Volver al Menú Principal", icon="🏠")
st.markdown("---")

tab1, tab2 = st.tabs(["Cartesianas a Polares", "Polares a Cartesianas"])

with tab1:
    st.header("Convertir Cartesianas (x, y) a Polares (r, θ)")
    st.write("Introduce un punto en coordenadas cartesianas para obtener su representación polar.")

    # --- Entradas de Usuario ---
    st.subheader("1. Punto Cartesiano de Entrada")
    col1, col2 = st.columns(2)
    with col1:
        x_in = st.number_input("Coordenada x", value=3.0, format="%.2f", key="cart_x")
    with col2:
        y_in = st.number_input("Coordenada y", value=4.0, format="%.2f", key="cart_y")

    if st.button("Convertir a Polares", key="btn_to_polar"):
        st.markdown("---")
        st.subheader("2. Resultados de la Conversión")

        # --- Cálculo ---
        r_out = np.sqrt(x_in**2 + y_in**2)
        theta_rad_out = np.arctan2(y_in, x_in)
        theta_deg_out = np.rad2deg(theta_rad_out)

        st.markdown("#### Fórmulas Utilizadas")
        st.latex(r"r = \sqrt{x^2 + y^2}")
        st.latex(r"\theta = \arctan\left(\frac{y}{x}\right)")

        st.markdown("#### Coordenadas Polares Resultantes")
        col_r, col_theta1, col_theta2 = st.columns(3)
        col_r.metric("Radio (r)", f"{r_out:.4f}")
        col_theta1.metric("Ángulo (θ) en Radianes", f"{theta_rad_out:.4f} rad")
        col_theta2.metric("Ángulo (θ) en Grados", f"{theta_deg_out:.2f}°")

        # --- Gráfica ---
        st.markdown("---")
        st.subheader("3. Visualización Gráfica")
        traces = []
        # Punto
        traces.append(go.Scatter(x=[x_in], y=[y_in], mode='markers+text', name='Punto',
                                 marker=dict(color='crimson', size=12),
                                 text=[f'({x_in:.2f}, {y_in:.2f})'], textposition="top right"))
        # Radio (línea desde el origen)
        traces.append(go.Scatter(x=[0, x_in], y=[0, y_in], mode='lines', name=f'Radio r={r_out:.2f}',
                                 line=dict(color='royalblue', dash='dash')))
        # Arco del ángulo
        theta_arc = np.linspace(0, theta_rad_out, 50)
        r_arc = r_out * 0.3 # Radio pequeño para el arco
        traces.append(go.Scatter(x=r_arc * np.cos(theta_arc), y=r_arc * np.sin(theta_arc),
                                 mode='lines', name=f'Ángulo θ={theta_deg_out:.1f}°', line=dict(color='green')))

        fig = create_plotly_figure(traces, title=f"Punto ({x_in:.2f}, {y_in:.2f}) a Coordenadas Polares")
        st.plotly_chart(fig, use_container_width=True)

with tab2:
    st.header("Convertir Polares (r, θ) a Cartesianas (x, y)")
    st.write("Introduce un punto en coordenadas polares para obtener su representación cartesiana.")

    # --- Entradas de Usuario ---
    st.subheader("1. Punto Polar de Entrada")
    col1, col2, col3 = st.columns(3)
    with col1:
        r_in = st.number_input("Radio (r)", value=5.0, min_value=0.0, format="%.2f", key="polar_r")
    with col2:
        theta_in = st.number_input("Ángulo (θ)", value=45.0, format="%.2f", key="polar_theta")
    with col3:
        angle_unit = st.radio("Unidad del ángulo", ["Grados", "Radianes"], key="polar_unit")

    if st.button("Convertir a Cartesianas", key="btn_to_cart"):
        st.markdown("---")
        st.subheader("2. Resultados de la Conversión")

        # --- Cálculo ---
        if angle_unit == "Grados":
            theta_rad_in = np.deg2rad(theta_in)
        else:
            theta_rad_in = theta_in

        x_out = r_in * np.cos(theta_rad_in)
        y_out = r_in * np.sin(theta_rad_in)

        st.markdown("#### Fórmulas Utilizadas")
        st.latex(r"x = r \cdot \cos(\theta)")
        st.latex(r"y = r \cdot \sin(\theta)")

        st.markdown("#### Coordenadas Cartesianas Resultantes")
        col_x, col_y = st.columns(2)
        col_x.metric("Coordenada x", f"{x_out:.4f}")
        col_y.metric("Coordenada y", f"{y_out:.4f}")

        # --- Gráfica ---
        st.markdown("---")
        st.subheader("3. Visualización Gráfica")
        traces = []
        # Punto
        traces.append(go.Scatter(x=[x_out], y=[y_out], mode='markers+text', name='Punto',
                                 marker=dict(color='crimson', size=12),
                                 text=[f'({x_out:.2f}, {y_out:.2f})'], textposition="top right"))
        # Radio (línea desde el origen)
        traces.append(go.Scatter(x=[0, x_out], y=[0, y_out], mode='lines', name=f'Radio r={r_in:.2f}',
                                 line=dict(color='royalblue', dash='dash')))
        # Arco del ángulo
        theta_arc = np.linspace(0, theta_rad_in, 50)
        r_arc = r_in * 0.3 # Radio pequeño para el arco
        traces.append(go.Scatter(x=r_arc * np.cos(theta_arc), y=r_arc * np.sin(theta_arc),
                                 mode='lines', name=f'Ángulo θ={np.rad2deg(theta_rad_in):.1f}°', line=dict(color='green')))

        fig = create_plotly_figure(traces, title=f"Punto (r={r_in:.2f}, θ={theta_in:.2f}°) a Coordenadas Cartesianas")
        st.plotly_chart(fig, use_container_width=True)


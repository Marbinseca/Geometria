import streamlit as st
import numpy as np
import plotly.graph_objects as go
from utils.ui_components import create_plotly_figure, point_input_widgets

st.set_page_config(page_title="Rectas Paralelas y Perpendiculares", page_icon="📐", layout="wide")

st.title("Calculadora de Rectas Paralelas y Perpendiculares")
st.write("Define una recta original (con dos puntos) y un punto exterior. La calculadora encontrará las ecuaciones de las rectas paralela y perpendicular que pasan por ese punto.")

st.page_link("app.py", label="← Volver al Menú Principal", icon="🏠")
st.markdown("---")

# --- Entradas de Usuario ---
st.subheader("1. Define la Recta Original (L₁)")
x1, y1, x2, y2 = point_input_widgets(key_prefix="original_line", p1_defaults=(0.0, 1.0), p2_defaults=(4.0, 3.0))

st.subheader("2. Define el Punto Exterior (P)")
col1, col2, _ = st.columns(3)
with col1:
    px = st.number_input("Coordenada x del punto P", value=2.0, format="%.2f", key="ext_px")
with col2:
    py = st.number_input("Coordenada y del punto P", value=5.0, format="%.2f", key="ext_py")

# --- Cálculo y Visualización ---
if st.button("Calcular y Graficar Rectas"):
    st.markdown("---")
    st.subheader("Resultados")

    # --- Cálculo de la recta original ---
    delta_x = x2 - x1
    delta_y = y2 - y1

    if delta_x == 0:
        m_orig = np.inf # Pendiente indefinida
        b_orig = np.nan
        eq_orig_str = f"x = {x1:.2f}"
    else:
        m_orig = delta_y / delta_x
        b_orig = y1 - m_orig * x1
        eq_orig_str = f"y = {m_orig:.2f}x + {b_orig:+.2f}"

    st.markdown(f"**Recta Original (L₁):** ${eq_orig_str}$ (pasa por P₁ y P₂)")

    # --- Cálculo de la recta paralela ---
    st.markdown("#### Recta Paralela (L₂)")
    m_para = m_orig
    if np.isinf(m_para):
        b_para = np.nan
        eq_para_str = f"x = {px:.2f}"
    else:
        b_para = py - m_para * px
        eq_para_str = f"y = {m_para:.2f}x + {b_para:+.2f}"
    st.success(f"La ecuación de la recta paralela que pasa por P({px:.2f}, {py:.2f}) es: **${eq_para_str}$**")

    # --- Cálculo de la recta perpendicular ---
    st.markdown("#### Recta Perpendicular (L₃)")
    if np.isinf(m_orig): # Original es vertical
        m_perp = 0
        b_perp = py
        eq_perp_str = f"y = {py:.2f}"
    elif m_orig == 0: # Original es horizontal
        m_perp = np.inf
        b_perp = np.nan
        eq_perp_str = f"x = {px:.2f}"
    else:
        m_perp = -1 / m_orig
        b_perp = py - m_perp * px
        eq_perp_str = f"y = {m_perp:.2f}x + {b_perp:+.2f}"
    st.success(f"La ecuación de la recta perpendicular que pasa por P({px:.2f}, {py:.2f}) es: **${eq_perp_str}$**")

    # --- Gráfica ---
    st.markdown("---")
    st.subheader("Visualización Gráfica")
    traces = []

    # Rango de la gráfica
    all_x = [x1, x2, px]
    x_min, x_max = min(all_x) - 5, max(all_x) + 5
    x_vals = np.linspace(x_min, x_max, 100)
    all_y = [y1, y2, py]
    y_min, y_max = min(all_y) - 5, max(all_y) + 5

    # 1. Trazas de las rectas
    if not np.isinf(m_orig): traces.append(go.Scatter(x=x_vals, y=m_orig * x_vals + b_orig, mode='lines', name=f'L₁: {eq_orig_str}', line=dict(color='grey')))
    else: traces.append(go.Scatter(x=[x1, x1], y=[y_min, y_max], mode='lines', name=f'L₁: {eq_orig_str}', line=dict(color='grey')))

    if not np.isinf(m_para): traces.append(go.Scatter(x=x_vals, y=m_para * x_vals + b_para, mode='lines', name=f'L₂: {eq_para_str}', line=dict(color='blue', dash='dash')))
    else: traces.append(go.Scatter(x=[px, px], y=[y_min, y_max], mode='lines', name=f'L₂: {eq_para_str}', line=dict(color='blue', dash='dash')))

    if not np.isinf(m_perp): traces.append(go.Scatter(x=x_vals, y=m_perp * x_vals + b_perp, mode='lines', name=f'L₃: {eq_perp_str}', line=dict(color='red', dash='dash')))
    else: traces.append(go.Scatter(x=[px, px], y=[y_min, y_max], mode='lines', name=f'L₃: {eq_perp_str}', line=dict(color='red', dash='dash')))

    # 2. Puntos
    traces.append(go.Scatter(x=[x1, x2], y=[y1, y2], mode='markers', name='Puntos L₁', marker=dict(color='black', size=10)))
    traces.append(go.Scatter(x=[px], y=[py], mode='markers+text', name='Punto Exterior', marker=dict(color='crimson', size=12, symbol='star'), text=[f'P({px:.2f}, {py:.2f})'], textposition="top right"))

    # Crear figura
    fig = create_plotly_figure(traces=traces, title="Rectas Paralelas y Perpendiculares")
    st.plotly_chart(fig, use_container_width=True)
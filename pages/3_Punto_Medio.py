import streamlit as st
import numpy as np
import plotly.graph_objects as go
from utils.ui_components import point_input_widgets, create_plotly_figure

st.set_page_config(page_title="Cálculo de Punto Medio", page_icon="📐", layout="wide")

st.title("Calculadora de Punto Medio")
st.write("Introduce las coordenadas de dos puntos para encontrar el punto medio del segmento que los une.")

# --- Boton para volver al menú principal ---
st.page_link("app.py", label="← Volver al Menú Principal", icon="🏠")
st.markdown("---")
st.write("Aquí encontrarás un resumen de las fórmulas y conceptos clave utilizados en esta aplicación.")

# --- Entradas de Usuario ---
x1, y1, x2, y2 = point_input_widgets(key_prefix="pm", p1_defaults=(-2.0, 1.0), p2_defaults=(4.0, 3.0))

# --- Cálculo y Visualización ---
if st.button("Calcular Punto Medio y Graficar"):
    # Cálculo de las coordenadas del punto medio
    xm = (x1 + x2) / 2
    ym = (y1 + y2) / 2

    st.markdown("---")
    st.subheader("Resultados del Cálculo")

    st.markdown("#### Paso a Paso")

    # Paso 1: Fórmula
    st.write("1. Partimos de la fórmula del punto medio (Pₘ):")
    st.latex(r"P_m = \left( \frac{x_1 + x_2}{2}, \frac{y_1 + y_2}{2} \right)")

    # Paso 2: Sustitución
    st.write(f"2. Sustituimos los valores de los puntos P₁({x1}, {y1}) y P₂({x2}, {y2}):")
    st.latex(fr"P_m = \left( \frac{{{x1} + ({x2})}}{2}, \frac{{{y1} + ({y2})}}{2} \right)")

    # Paso 3: Operación de suma
    st.write("3. Realizamos las sumas en los numeradores:")
    st.latex(fr"P_m = \left( \frac{{{x1 + x2:.2f}}}{2}, \frac{{{y1 + y2:.2f}}}{2} \right)")

    # Paso 4: División
    st.write("4. Finalmente, dividimos por 2 para encontrar las coordenadas:")
    st.latex(fr"P_m = ({xm:.2f}, {ym:.2f})")

    st.success(f"Las coordenadas del punto medio son: **({xm:.2f}, {ym:.2f})**")
    st.metric(label="Punto Medio (Pₘ)", value=f"({xm:.2f}, {ym:.2f})")

    # --- Preparación de datos para la Gráfica ---
    traces = []

    # 1. Añadir el segmento de línea que une los dos puntos
    traces.append(go.Scatter(x=[x1, x2], y=[y1, y2], mode='lines', name='Segmento', line=dict(color='lightgrey', width=2, dash='dash')))

    # 2. Añadir los puntos P1 y P2 a la gráfica
    traces.append(go.Scatter(
        x=[x1, x2], y=[y1, y2],
        mode='markers+text', name='Puntos Extremos',
        marker=dict(color='crimson', size=12),
        text=[f'P₁({x1}, {y1})', f'P₂({x2}, {y2})'],
        textposition="top center"
    ))

    # 3. Añadir el Punto Medio a la gráfica
    traces.append(go.Scatter(
        x=[xm], y=[ym],
        mode='markers+text', name='Punto Medio',
        marker=dict(color='mediumseagreen', size=14, symbol='diamond'),
        text=[f'<b>Pₘ({xm:.2f}, {ym:.2f})</b>'],
        textposition="bottom center"
    ))

    # 4. Crear y mostrar la figura usando la función reutilizable
    fig = create_plotly_figure(
        traces=traces,
        title="Visualización del Punto Medio"
    )

    st.plotly_chart(fig, use_container_width=True)
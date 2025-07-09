import streamlit as st
import numpy as np
import plotly.graph_objects as go
import math
from utils.ui_components import point_input_widgets, create_plotly_figure

st.set_page_config(page_title="Cálculo de Distancia", page_icon="📐", layout="wide")

st.title("Calculadora de Distancia entre Dos Puntos")
st.write("Introduce las coordenadas de dos puntos para calcular la distancia que los separa.")

# --- Boton para volver al menú principal ---
st.page_link("app.py", label="← Volver al Menú Principal", icon="🏠")
st.markdown("---")
st.write("Aquí encontrarás un resumen de las fórmulas y conceptos clave utilizados en esta aplicación.")

# --- Entradas de Usuario (reutilizamos la estructura) ---
x1, y1, x2, y2 = point_input_widgets(key_prefix="dist", p1_defaults=(1.0, 1.0), p2_defaults=(5.0, 4.0))

# --- Cálculo y Visualización ---
if st.button("Calcular Distancia y Graficar"):
    # Usamos numpy para manejar los puntos
    p1 = np.array([x1, y1])
    p2 = np.array([x2, y2])

    # Cálculo de deltas
    delta_x = p2[0] - p1[0]
    delta_y = p2[1] - p1[1]

    # Cálculo de la distancia usando numpy
    # Es el equivalente a sqrt(delta_x**2 + delta_y**2)
    distance = np.linalg.norm(p2 - p1)

    st.markdown("---")
    st.subheader("Resultados del Cálculo")

    st.markdown("#### Paso a Paso")

    # Paso 1: Fórmula
    st.write("1. Partimos de la fórmula de la distancia euclidiana:")
    st.latex(r"d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}")

    # Paso 2: Sustitución
    st.write(f"2. Sustituimos los valores de los puntos P₁({x1}, {y1}) y P₂({x2}, {y2}):")
    st.latex(fr"d = \sqrt{{({x2} - ({x1}))^2 + ({y2} - ({y1}))^2}}")

    # Paso 3: Operación de resta
    st.write("3. Realizamos las restas dentro de los paréntesis:")
    st.latex(fr"d = \sqrt{{({delta_x:.2f})^2 + ({delta_y:.2f})^2}}")

    # Paso 4: Potencias
    st.write("4. Elevamos al cuadrado cada término:")
    st.latex(fr"d = \sqrt{{{delta_x**2:.2f} + {delta_y**2:.2f}}}")

    # Paso 5: Suma
    st.write("5. Sumamos los resultados:")
    st.latex(fr"d = \sqrt{{{delta_x**2 + delta_y**2:.2f}}}")

    # Paso 6: Raíz cuadrada
    st.write("6. Finalmente, calculamos la raíz cuadrada:")
    st.latex(fr"d \approx {distance:.4f}")
    st.success(f"La distancia entre los dos puntos es: **{distance:.4f}**")
    st.metric(label="Distancia (d)", value=f"{distance:.4f}")

    # --- Preparación de datos para la Gráfica ---
    traces = []
    annotations = []

    # 1. Añadir el segmento de línea que une los dos puntos
    traces.append(go.Scatter(x=[x1, x2], y=[y1, y2], mode='lines', name='Distancia', line=dict(color='royalblue', width=3, dash='dash')))

    # 2. Añadir los puntos P1 y P2 a la gráfica
    traces.append(go.Scatter(
        x=[x1, x2], y=[y1, y2],
        mode='markers+text', name='Puntos',
        marker=dict(color='crimson', size=12),
        text=[f'P₁({x1}, {y1})', f'P₂({x2}, {y2})'],
        textposition="bottom center"
    ))

    # 3. Añadir una anotación en el punto medio para mostrar la distancia
    annotations.append(dict(
        x=(x1 + x2) / 2, y=(y1 + y2) / 2,
        text=f"<b>d ≈ {distance:.2f}</b>",
        showarrow=False, yshift=15,
        font=dict(family="Arial, sans-serif", size=14, color="navy"),
        bgcolor="rgba(255, 255, 255, 0.7)"
    ))

    # 4. Crear y mostrar la figura usando la función reutilizable
    fig = create_plotly_figure(
        traces=traces,
        title=f"Visualización de la Distancia (d ≈ {distance:.2f})",
        annotations=annotations
    )

    st.plotly_chart(fig, use_container_width=True)
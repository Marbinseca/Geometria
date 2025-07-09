import streamlit as st
import numpy as np
import plotly.graph_objects as go
from utils.ui_components import point_input_widgets, create_plotly_figure

st.set_page_config(page_title="Cálculo de Pendiente", page_icon="📐", layout="wide")

st.title("Calculadora de Pendiente de una Recta")
st.write("Introduce las coordenadas de dos puntos para calcular la pendiente de la recta que los une.")

# --- Boton para volver al menú principal ---
st.page_link("app.py", label="← Volver al Menú Principal", icon="🏠")
st.markdown("---")
st.write("Aquí encontrarás un resumen de las fórmulas y conceptos clave utilizados en esta aplicación.")

# --- Entradas de Usuario ---
x1, y1, x2, y2 = point_input_widgets(key_prefix="slope", p1_defaults=(0.0, 0.0), p2_defaults=(5.0, 4.0))

# --- Cálculo y Visualización ---
if st.button("Calcular Pendiente y Graficar"):
    # Usamos numpy como solicitaste para manejar los puntos
    p1 = np.array([x1, y1])
    p2 = np.array([x2, y2])

    delta_x = p2[0] - p1[0]
    delta_y = p2[1] - p1[1]

    st.markdown("---")
    st.subheader("Resultados del Cálculo")

    st.markdown("#### Paso a Paso")

    # Paso 1: Fórmula
    st.write("1. Partimos de la fórmula de la pendiente:")
    st.latex(r"m = \frac{y_2 - y_1}{x_2 - x_1}")

    # Paso 2: Sustitución
    st.write(f"2. Sustituimos los valores de los puntos P₁({x1}, {y1}) y P₂({x2}, {y2}):")
    # Usamos paréntesis para manejar correctamente los números negativos
    st.latex(fr"m = \frac{{{y2} - ({y1})}}{{{x2} - ({x1})}}")

    # Paso 3: Operación
    st.write("3. Realizamos las operaciones de resta en el numerador y denominador:")
    st.latex(fr"m = \frac{{{delta_y:.2f}}}{{{delta_x:.2f}}}")

    # Paso 4: Resultado final
    st.write("4. Finalmente, calculamos la división para obtener la pendiente:")

    # Manejo del caso de una línea vertical (pendiente indefinida)
    if delta_x == 0:
        st.latex(r"m \rightarrow \text{Indefinida}")
        st.error("La división por cero no está definida. La recta es vertical y su pendiente es **indefinida**.")
        slope_text = "Indefinida"
    else:
        slope = delta_y / delta_x
        st.latex(fr"m = {slope:.4f}")
        st.success(f"El valor final de la pendiente es **{slope:.4f}**.")
        st.metric(label="Pendiente (m)", value=f"{slope:.4f}")
        slope_text = f"{slope:.4f}"

    # --- Preparación de datos para la Gráfica ---
    traces = []
    annotations = []

    # 1. Añadir los puntos P1 y P2 a la gráfica
    traces.append(go.Scatter(
        x=[p1[0], p2[0]], 
        y=[p1[1], p2[1]], 
        mode='markers+text', 
        name='Puntos',
        marker=dict(color='crimson', size=12),
        text=[f'P₁({x1}, {y1})', f'P₂({x2}, {y2})'],
        textposition="top right"
    ))

    # 2. Dibujar la línea que se extiende más allá de los puntos
    x_range = np.array([min(p1[0], p2[0]) - 2, max(p1[0], p2[0]) + 2])

    if delta_x == 0: # Caso de línea vertical
        y_range = np.array([min(p1[1], p2[1]) - 2, max(p1[1], p2[1]) + 2])
        traces.append(go.Scatter(x=[p1[0], p1[0]], y=y_range, mode='lines', name='Recta', line=dict(dash='dash')))
    else: # Caso general
        b = p1[1] - slope * p1[0]
        y_range = slope * x_range + b
        traces.append(go.Scatter(x=x_range, y=y_range, mode='lines', name='Recta', line=dict(dash='dash')))

    # 3. Añadir una anotación en el punto medio para mostrar la pendiente
    annotations.append(dict(
        x=(x1 + x2) / 2, y=(y1 + y2) / 2,
        text=f"<b>m = {slope_text}</b>",
        showarrow=False, yshift=15,
        font=dict(family="Arial, sans-serif", size=14, color="purple"),
        bgcolor="rgba(255, 255, 255, 0.7)"
    ))

    # 4. Crear y mostrar la figura usando la función reutilizable
    fig = create_plotly_figure(
        traces=traces,
        title=f"Visualización de la Recta (m = {slope_text})",
        annotations=annotations
    )

    st.plotly_chart(fig, use_container_width=True)
import streamlit as st
import numpy as np
import plotly.graph_objects as go
from utils.ui_components import point_input_widgets

st.set_page_config(page_title="Ecuación de la Recta (2 Puntos)", page_icon="📐", layout="wide")

st.title("Calcular Ecuación de la Recta a partir de Dos Puntos")
st.write("Introduce las coordenadas de dos puntos para encontrar la pendiente y la ecuación de la recta que los une.")

# --- Boton para volver al menú principal ---
st.page_link("app.py", label="← Volver al Menú Principal", icon="🏠")
st.markdown("---")
st.write("Aquí encontrarás un resumen de las fórmulas y conceptos clave utilizados en esta aplicación.")

# --- Entradas de Usuario ---
x1, y1, x2, y2 = point_input_widgets(key_prefix="eq_from_points", p1_defaults=(1.0, 2.0), p2_defaults=(4.0, 8.0))

# --- Cálculo y Visualización ---
if st.button("Calcular Ecuación y Graficar"):
    p1 = np.array([x1, y1])
    p2 = np.array([x2, y2])

    delta_x = p2[0] - p1[0]
    delta_y = p2[1] - p1[1]

    st.markdown("---")
    st.subheader("Resultados del Cálculo")

    # --- PASO 1: CÁLCULO DE LA PENDIENTE ---
    st.markdown("#### Paso 1: Calcular la Pendiente (m)")
    st.latex(r"m = \frac{y_2 - y_1}{x_2 - x_1} = \frac{" + f"{y2} - ({y1})"+r"}{"+f"{x2} - ({x1})"+r"} = \frac{"+f"{delta_y:.2f}"+r"}{"+f"{delta_x:.2f}"+r"}")

    # Manejo de casos
    if delta_x == 0:
        st.error("La recta es vertical (pendiente indefinida).")
        slope_text = "Indefinida"
        equation_str = f"x = {x1:.2f}"
        st.markdown("#### Paso 2: Determinar la Ecuación")
        st.write("Como la recta es vertical, su ecuación es simplemente:")
        st.latex(equation_str)

    else:
        slope = delta_y / delta_x
        st.latex(f"m = {slope:.4f}")
        slope_text = f"{slope:.4f}"

        # --- PASO 2: CÁLCULO DE LA ECUACIÓN ---
        st.markdown("#### Paso 2: Calcular el Intercepto (b)")
        st.write("Usamos la forma punto-pendiente `y = mx + b` y despejamos `b` con el Punto 1:")
        st.latex(r"b = y_1 - m \cdot x_1")
        st.write("Sustituimos los valores:")
        b = y1 - slope * x1
        st.latex(f"b = {y1:.2f} - ({slope:.2f}) \\cdot ({x1:.2f}) = {b:.2f}")

        st.markdown("#### Paso 3: Ecuación Final")
        signo = "+" if b >= 0 else "-"
        b_abs = abs(b)
        equation_str = f"y = {slope:.2f}x {signo} {b_abs:.2f}"
        st.write("Con la pendiente (m) y el intercepto (b), la ecuación es:")
        st.latex(equation_str)

    st.success(f"La ecuación de la recta es: **${equation_str}$**")

    # --- Gráfica con Plotly ---
    st.subheader("Visualización Gráfica")
    fig = go.Figure()

    # 1. Dibujar la línea extendida
    x_min_val = min(p1[0], p2[0]) - 2
    x_max_val = max(p1[0], p2[0]) + 2
    x_range = np.array([x_min_val, x_max_val])

    if delta_x == 0: # Caso de línea vertical
        y_min_val = min(p1[1], p2[1]) - 2
        y_max_val = max(p1[1], p2[1]) + 2
        fig.add_trace(go.Scatter(x=[p1[0], p1[0]], y=[y_min_val, y_max_val], mode='lines', name='Recta', line=dict(dash='dash')))
    else: # Caso general
        y_range = slope * x_range + b
        fig.add_trace(go.Scatter(x=x_range, y=y_range, mode='lines', name='Recta', line=dict(dash='dash')))

    # 2. Añadir los puntos P1 y P2
    fig.add_trace(go.Scatter(
        x=[p1[0], p2[0]], y=[p1[1], p2[1]], mode='markers+text', name='Puntos',
        marker=dict(color='crimson', size=12),
        text=[f'P₁({x1:.2f}, {y1:.2f})', f'P₂({x2:.2f}, {y2:.2f})'],
        textposition="top right"
    ))

    # 3. Añadir anotaciones
    # Anotación para la pendiente
    fig.add_annotation(
        x=(x1 + x2) / 2, y=(y1 + y2) / 2, text=f"<b>m = {slope_text}</b>",
        showarrow=False, yshift=15, font=dict(family="Arial", size=14, color="purple"),
        bgcolor="rgba(255, 255, 255, 0.7)"
    )

    # Anotación para el intercepto (si existe)
    if delta_x != 0:
        fig.add_trace(go.Scatter(
            x=[0], y=[b], mode='markers+text', name='Intercepto en y',
            marker=dict(color='green', size=10, symbol='circle'),
            text=[f'b = {b:.2f}'], textposition="bottom left"
        ))

    # 4. Configurar el diseño de la gráfica
    fig.update_layout(
        title=f"Gráfica de ${equation_str}$",
        xaxis_title="Eje X", yaxis_title="Eje Y",
        xaxis=dict(scaleanchor="y", scaleratio=1),
        yaxis=dict(scaleanchor="x", scaleratio=1),
        legend=dict(yanchor="top", y=0.99, xanchor="left", x=0.01)
    )
    fig.update_xaxes(zeroline=True, zerolinewidth=2, zerolinecolor='LightGrey')
    fig.update_yaxes(zeroline=True, zerolinewidth=2, zerolinecolor='LightGrey')

    st.plotly_chart(fig, use_container_width=True)


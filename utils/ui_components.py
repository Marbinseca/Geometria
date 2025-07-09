import streamlit as st
import plotly.graph_objects as go

def point_input_widgets(
    key_prefix: str,
    p1_defaults: tuple = (0.0, 0.0),
    p2_defaults: tuple = (5.0, 4.0)
):
    """
    Crea los widgets de entrada para dos puntos (P1 y P2) y devuelve sus coordenadas.

    Args:
        key_prefix (str): Un prefijo único para las claves de los widgets de Streamlit
                          para evitar conflictos entre páginas.
        p1_defaults (tuple): Valores por defecto para (x1, y1).
        p2_defaults (tuple): Valores por defecto para (x2, y2).

    Returns:
        tuple: Una tupla con las coordenadas (x1, y1, x2, y2).
    """
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Punto 1 (P₁)")
        x1 = st.number_input(
            "Coordenada x₁",
            value=float(p1_defaults[0]),
            format="%.2f",
            key=f"{key_prefix}_x1"
        )
        if not isinstance(x1, (int, float)):
            st.error("La coordenada x₁ debe ser un número.")
            x1 = p1_defaults[0]  # Restablecer al valor por defecto
        y1 = st.number_input(
            "Coordenada y₁",
            value=float(p1_defaults[1]),
            format="%.2f",
            key=f"{key_prefix}_y1"
        )
        if not isinstance(y1, (int, float)):
            st.error("La coordenada y₁ debe ser un número.")
            y1 = p1_defaults[1]

    with col2:
        st.subheader("Punto 2 (P₂)")
        x2 = st.number_input("Coordenada x₂", value=float(p2_defaults[0]), format="%.2f", key=f"{key_prefix}_x2")
        if not isinstance(x2, (int, float)):
            st.error("La coordenada x₂ debe ser un número.")
            x2 = p2_defaults[0]
        y2 = st.number_input("Coordenada y₂", value=float(p2_defaults[1]), format="%.2f", key=f"{key_prefix}_y2")
        if not isinstance(y2, (int, float)):
            st.error("La coordenada y₂ debe ser un número.")
            y2 = p2_defaults[1]

    return x1, y1, x2, y2

def create_plotly_figure(
    traces: list,
    title: str,
    annotations: list = None,
    xaxis_title: str = "Eje X",
    yaxis_title: str = "Eje Y"
):
    """
    Crea una figura de Plotly con una configuración estándar y trazas personalizadas.

    Args:
        traces (list): Una lista de trazas de Plotly (ej. [go.Scatter(...)]) para añadir a la figura.
        title (str): El título de la gráfica.
        annotations (list, optional): Una lista de diccionarios de anotaciones de Plotly. Defaults to None.
        xaxis_title (str, optional): Título del eje X. Defaults to "Eje X".
        yaxis_title (str, optional): Título del eje Y. Defaults to "Eje Y".

    Returns:
        go.Figure: El objeto de la figura de Plotly configurado.
    """
    fig = go.Figure()

    for trace in traces:
        fig.add_trace(trace)

    if annotations:
        for annotation in annotations:
            # Usamos ** para desempaquetar el diccionario de anotaciones
            fig.add_annotation(**annotation)

    fig.update_layout(
        title=title,
        xaxis_title=xaxis_title, yaxis_title=yaxis_title,
        xaxis=dict(scaleanchor="y", scaleratio=1),
        yaxis=dict(scaleanchor="x", scaleratio=1),
        legend=dict(yanchor="top", y=0.99, xanchor="left", x=0.01)
    )
    fig.update_xaxes(zeroline=True, zerolinewidth=2, zerolinecolor='LightGrey')
    fig.update_yaxes(zeroline=True, zerolinewidth=2, zerolinecolor='LightGrey')

    return fig
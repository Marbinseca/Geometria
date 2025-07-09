import streamlit as st
from PIL import Image
import os
import itertools

st.set_page_config(
    page_title="Geometría Interactiva",
    page_icon="📐",
    layout="wide"
)

# --- Cabecera con Logo y Título ---
col1, col2 = st.columns([1, 5])
with col1:
    try:
        image = Image.open('assets/logo.png')
        st.image(image, use_column_width='auto')
    except FileNotFoundError:
        # Si no se encuentra el logo, simplemente no se muestra.
        pass
with col2:
    st.title("Calculadora Geométrica Interactiva")
    st.markdown("Selecciona un tema para comenzar. Cada calculadora te guiará paso a paso y te mostrará una gráfica interactiva.")

st.markdown("---")

# --- Definición de las páginas/tarjetas de navegación ---
PAGE_GROUPS = {
    "Fundamentos del Plano Cartesiano": [
        {"title": "Pendiente de una Recta", "icon": "📈", "description": "Calcula la inclinación de una recta a partir de dos puntos.", "path": "pages/1_Pendiente.py"},
        {"title": "Distancia entre Puntos", "icon": "📏", "description": "Encuentra la longitud del segmento que une dos puntos.", "path": "pages/2_Distancia_entre_puntos.py"},
        {"title": "Punto Medio", "icon": "📍", "description": "Halla las coordenadas del punto que divide un segmento.", "path": "pages/3_Punto_Medio.py"},
    ],
    "Ecuaciones y Relaciones de la Recta": [
        {"title": "Ecuación: Pendiente-Intercepto", "icon": "✒️", "description": "Visualiza una recta a partir de su pendiente e intercepto.", "path": "pages/4_Ecuacion_de_la_Recta.py"},
        {"title": "Ecuación: Punto-Pendiente", "icon": "✍️", "description": "Encuentra la ecuación a partir de un punto y su pendiente.", "path": "pages/5_Ecuacion_Punto_Pendiente.py"},
        {"title": "Ecuación: Dos Puntos", "icon": "✍️", "description": "Obtén la ecuación de la recta que pasa por dos puntos.", "path": "pages/6_Ecuacion_desde_Puntos.py"},
        {"title": "Rectas Paralelas y Perpendiculares", "icon": "∥", "description": "Calcula rectas paralelas/perpendiculares por un punto.", "path": "pages/7_Rectas_Paralelas_y_Perpendiculares.py"},
    ],
    "Secciones Cónicas": [
        {"title": "Circunferencia", "icon": "⭕", "description": "Calcula la ecuación de una circunferencia.", "path": "pages/8_Ecuacion_de_la_Circunferencia.py"},
        {"title": "Parábola", "icon": "📡", "description": "Calcula la ecuación de una parábola.", "path": "pages/9_Ecuacion_de_la_Parabola.py"},
        {"title": "Elipse", "icon": "⬬", "description": "Calcula la ecuación de una elipse.", "path": "pages/10_Ecuacion_de_la_Elipse.py"},
        {"title": "Hipérbola", "icon": "⏳", "description": "Calcula la ecuación de una hipérbola.", "path": "pages/11_Ecuacion_de_la_Hiperbola.py"},
    ],
    "Otros Sistemas": [
        {"title": "Coordenadas Polares", "icon": "🧭", "description": "Convierte entre coordenadas cartesianas y polares.", "path": "pages/12_Coordenadas_Polares.py"},
    ],
    "Referencias": [
        {"title": "Teoría y Fórmulas", "icon": "📚", "description": "Consulta las definiciones y fórmulas clave.", "path": "pages/0_Teoria_y_Formulas.py"},
        {"title": "Acerca de", "icon": "ℹ️", "description": "Conoce el propósito del proyecto y las tecnologías utilizadas.", "path": "pages/13_Acerca_de.py"}
    ]
}

# --- Creación de la cuadrícula de tarjetas agrupadas ---
for group_title, pages_in_group in PAGE_GROUPS.items():
    st.subheader(group_title)

    num_cols = 3
    # Creamos un iterador para las páginas del grupo actual
    page_iterator = iter(pages_in_group)

    # Creamos filas de columnas hasta que se muestren todas las páginas del grupo
    while True:
        # Obtenemos el siguiente lote de páginas para la fila
        pages_for_row = list(itertools.islice(page_iterator, num_cols))
        if not pages_for_row:
            break  # Salimos del bucle si no hay más páginas

        cols = st.columns(num_cols)
        for i, page in enumerate(pages_for_row):
            with cols[i]:
                # Usamos un contenedor para crear el efecto de "tarjeta"
                with st.container(border=True):
                    st.markdown(f"### {page['icon']} {page['title']}")
                    st.markdown(f"<p style='color: #808389; min-height: 40px;'>{page['description']}</p>", unsafe_allow_html=True)
                    # Usamos un botón para la navegación, con una clave única basada en la ruta
                    if st.button("Ir a la calculadora →", key=f"nav_btn_{page['path']}", use_container_width=True):
                        st.switch_page(page["path"])

    st.markdown("---")
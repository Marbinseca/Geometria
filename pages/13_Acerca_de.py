import streamlit as st
from PIL import Image

st.set_page_config(page_title="Acerca de", page_icon="ℹ️", layout="wide")

st.title("ℹ️ Acerca de la Calculadora Geométrica Interactiva")

# --- Boton para volver al menú principal ---
st.page_link("app.py", label="← Volver al Menú Principal", icon="🏠")
st.markdown("---")

# --- Logo ---
try:
    image = Image.open('assets/logo.png')
    st.image(image, width=150)
except FileNotFoundError:
    pass

st.header("Propósito del Proyecto")
st.markdown("""
Esta aplicación web fue desarrollada como una herramienta educativa e interactiva para explorar los conceptos fundamentales de la **geometría analítica**. El objetivo es proporcionar a estudiantes y entusiastas una forma visual y práctica de:

- **Resolver problemas comunes:** Desde calcular la distancia entre dos puntos hasta encontrar la ecuación de una hipérbola.
- **Visualizar conceptos abstractos:** Cada calculadora genera una gráfica interactiva que ayuda a comprender la relación entre las ecuaciones y sus representaciones visuales.
- **Aprender paso a paso:** Las soluciones se presentan de forma detallada, mostrando las fórmulas y los cálculos intermedios.

Este proyecto busca hacer que el aprendizaje de la geometría sea más accesible, intuitivo y atractivo.
""")

st.markdown("---")

st.header("🛠️ Tecnologías Utilizadas")
st.markdown("""
La aplicación está construida enteramente en Python, utilizando un conjunto de librerías de código abierto de alto nivel:

- **[Streamlit](https://streamlit.io/):** Es el framework principal utilizado para construir la interfaz de usuario web. Permite crear aplicaciones web interactivas a partir de scripts de Python de una manera rápida y sencilla.
- **[Plotly](https://plotly.com/python/):** Es la librería encargada de generar todas las visualizaciones y gráficos interactivos. Su capacidad para crear gráficos de alta calidad es fundamental para el propósito educativo de la aplicación.
- **[NumPy](https://numpy.org/):** Se utiliza para realizar todos los cálculos numéricos de manera eficiente, especialmente en la generación de los puntos para las gráficas de las cónicas y las rectas.
- **[Pillow (PIL)](https://python-pillow.org/):** Se utiliza para el manejo de imágenes, como la carga del logo de la aplicación.
""")

st.markdown("---")
st.info("Desarrollado con ❤️ usando Python y Streamlit.")
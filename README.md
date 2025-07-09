# 📐 Calculadora de Geometría Analítica Interactiva

¡Bienvenido! Esta es una aplicación web interactiva construida con Streamlit para explorar y resolver problemas de geometría analítica. La herramienta está diseñada para ser educativa, proporcionando cálculos paso a paso y visualizaciones gráficas para cada concepto.

---

## 🚀 Demo en Vivo

¡Puedes probar la aplicación en vivo! Está desplegada en Streamlit Community Cloud.

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](geometria.streamlit.app/)

**[Haz clic aquí para abrir la aplicación](geometria.streamlit.app/)**

---

## ✨ Características

La aplicación incluye calculadoras para los siguientes temas:

*   **📚 Teoría y Fórmulas:** Un formulario de referencia rápida para los conceptos clave.
*   **📈 Pendiente de una Recta:** Calcula la inclinación de una recta a partir de dos puntos.
*   **📏 Distancia entre Puntos:** Encuentra la longitud del segmento que une dos puntos.
*   **📍 Punto Medio:** Halla las coordenadas del punto que divide un segmento en dos partes iguales.
*   **✒️ Ecuación de la Recta (Pendiente-Intercepto):** Visualiza una recta a partir de su pendiente (`m`) e intercepto (`b`).
*   **✍️ Ecuación de la Recta (Dos Puntos):** Obtén la ecuación de la recta que pasa por dos puntos.
*   **🧭 Coordenadas Polares:** Convierte entre coordenadas cartesianas y polares.
*   **⭕ Circunferencia:** Calcula y grafica la ecuación de una circunferencia.
*   **📡 Parábola:** Calcula y grafica la ecuación de una parábola.
*   **⬬ Elipse:** Calcula y grafica la ecuación de una elipse.
*   **⏳ Hipérbola:** Calcula y grafica la ecuación de una hipérbola.

---

## 🚀 Cómo Empezar

Sigue estos pasos para ejecutar la aplicación en tu máquina local.

### Prerrequisitos

*   Python 3.8 o superior.
*   `pip` y `venv` para la gestión de paquetes y entornos virtuales.

### Instalación y Ejecución

1.  **Clona el repositorio:**
    ```bash
    git clone <URL-DEL-REPOSITORIO>
    cd Geometria
    ```

2.  **Crea y activa un entorno virtual:**
    *   En Windows:
        ```bash
        python -m venv venv
        .\venv\Scripts\activate
        ```
    *   En macOS/Linux:
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```

3.  **Instala las dependencias:**
    El proyecto utiliza varias librerías de Python. Instálalas usando el archivo `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Ejecuta la aplicación Streamlit:**
    Una vez instaladas las dependencias, inicia la aplicación con el siguiente comando:
    ```bash
    streamlit run app.py
    ```
    ¡Tu navegador se abrirá automáticamente con la aplicación en ejecución!

---

## 📂 Estructura del Proyecto

```
Geometria/
├── assets/
│   └── logo.png          # Logo y otros recursos gráficos
├── pages/
│   ├── 0_Teoria_y_Formulas.py
│   └── ...               # Cada archivo es una página/calculadora
├── utils/
│   └── ui_components.py  # Componentes de UI reutilizables
├── app.py                # Página principal y menú de navegación
├── requirements.txt      # Dependencias del proyecto
└── README.md             # Este archivo
```

---

## 🛠️ Tecnologías Utilizadas

*   **Streamlit:** Para la creación de la interfaz web interactiva.
*   **Plotly:** Para la generación de gráficos dinámicos y visualizaciones.
*   **NumPy:** Para cálculos numéricos eficientes.
*   **Pillow:** Para el manejo de imágenes.
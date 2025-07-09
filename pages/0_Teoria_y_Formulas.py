import streamlit as st

st.set_page_config(page_title="Formulario de Geometría", page_icon="📐", layout="wide")

st.title("Formulario y Teoría de Geometría Analítica")

# --- Boton para volver al menú principal ---
st.page_link("app.py", label="← Volver al Menú Principal", icon="🏠")
st.markdown("---")
st.write("Aquí encontrarás un resumen de las fórmulas y conceptos clave utilizados en esta aplicación.")

# --- Pendiente ---
with st.expander("1. Pendiente de una Recta", expanded=True):
    st.subheader("Definición")
    st.markdown("""
    La **pendiente (m)** de una recta es una medida de su inclinación. Representa el cambio en la coordenada vertical (y) por cada unidad de cambio en la coordenada horizontal (x).
    - Una pendiente positiva indica que la recta sube de izquierda a derecha.
    - Una pendiente negativa indica que la recta baja de izquierda a derecha.
    - Una pendiente de cero indica una recta horizontal.
    - Una pendiente indefinida indica una recta vertical.
    """)
    
    st.subheader("Fórmula")
    st.markdown("Dados dos puntos $P_1(x_1, y_1)$ y $P_2(x_2, y_2)$:")
    st.latex(r"m = \frac{\Delta y}{\Delta x} = \frac{y_2 - y_1}{x_2 - x_1}")

# --- Distancia ---
with st.expander("2. Distancia entre Dos Puntos"):
    st.subheader("Definición")
    st.markdown("""
    La **distancia euclidiana (d)** entre dos puntos en un plano es la longitud del segmento de recta que los une. Se calcula utilizando el Teorema de Pitágoras.
    """)
    
    st.subheader("Fórmula")
    st.markdown("Dados dos puntos $P_1(x_1, y_1)$ y $P_2(x_2, y_2)$:")
    st.latex(r"d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}")

# --- Punto Medio ---
with st.expander("3. Punto Medio de un Segmento"):
    st.subheader("Definición")
    st.markdown("""
    El **punto medio (Pₘ)** de un segmento de recta es el punto que se encuentra a la misma distancia de ambos extremos. Sus coordenadas son el promedio de las coordenadas de los puntos extremos.
    """)
    
    st.subheader("Fórmula")
    st.markdown("Dados dos puntos $P_1(x_1, y_1)$ y $P_2(x_2, y_2)$:")
    st.latex(r"P_m = \left( \frac{x_1 + x_2}{2}, \frac{y_1 + y_2}{2} \right)")

# --- Ecuación de la Recta ---
with st.expander("4. Ecuación de la Recta"):
    st.subheader("Forma Pendiente-Intercepto")
    st.markdown("""
    Esta es una de las formas más comunes para expresar la ecuación de una recta. Es útil porque muestra directamente la pendiente y el punto donde la recta cruza el eje y.
    - **m**: es la pendiente de la recta.
    - **b**: es el intercepto en el eje y (el valor de y cuando x=0).
    """)
    st.latex(r"y = mx + b")

    st.subheader("Forma Punto-Pendiente")
    st.markdown("""
    Esta forma es útil cuando se conocen un punto $(x_1, y_1)$ por el que pasa la recta y su pendiente **m**. Es la base para encontrar la ecuación general de la recta.
    """)
    st.latex(r"y - y_1 = m(x - x_1)")


# --- Ecuación de la Circunferencia ---
with st.expander("5. Ecuación de la Circunferencia"):
    st.subheader("Definición")
    st.markdown("""
    Una circunferencia es el conjunto de todos los puntos en un plano que están a una distancia fija (llamada radio) de un punto fijo (llamado centro).
    """)
    
    st.subheader("Ecuación Estándar (Ordinaria)")
    st.markdown("Con centro en $(h, k)$ y radio $r$:")
    st.latex(r"(x - h)^2 + (y - k)^2 = r^2")
    
    st.subheader("Ecuación General")
    st.markdown("Es el resultado de expandir la ecuación estándar. Tiene la forma:")
    st.latex(r"x^2 + y^2 + Dx + Ey + F = 0")

# --- Parábola ---
with st.expander("6. Ecuación de la Parábola"):
    st.subheader("Definición")
    st.markdown("""
    Una parábola es el conjunto de todos los puntos que son equidistantes de un punto fijo (el **foco**) y una línea fija (la **directriz**).
    """)
    st.subheader("Ecuación Estándar con Vértice en (h, k)")
    st.markdown("Parábola Vertical:")
    st.latex(r"(x - h)^2 = 4p(y - k)")
    st.markdown("Parábola Horizontal:")
    st.latex(r"(y - k)^2 = 4p(x - h)")
    st.markdown("Donde **p** es la distancia del vértice al foco (y al directriz).")

# --- Elipse ---
with st.expander("7. Ecuación de la Elipse"):
    st.subheader("Definición")
    st.markdown("""
    Una elipse es el conjunto de todos los puntos para los cuales la suma de las distancias a dos puntos fijos (los **focos**) es constante.
    """)
    st.subheader("Ecuación Estándar con Centro en (h, k)")
    st.latex(r"\frac{(x - h)^2}{a^2} + \frac{(y - k)^2}{b^2} = 1")
    st.markdown("Donde **a** es el semieje horizontal y **b** es el semieje vertical.")

# --- Hipérbola ---
with st.expander("8. Ecuación de la Hipérbola"):
    st.subheader("Definición")
    st.markdown("""
    Una hipérbola es el conjunto de todos los puntos para los cuales la diferencia absoluta de las distancias a dos puntos fijos (los **focos**) es constante.
    """)
    st.subheader("Ecuación Estándar con Centro en (h, k)")
    st.markdown("Hipérbola Horizontal:")
    st.latex(r"\frac{(x - h)^2}{a^2} - \frac{(y - k)^2}{b^2} = 1")
    st.markdown("Hipérbola Vertical:")
    st.latex(r"\frac{(y - k)^2}{a^2} - \frac{(x - h)^2}{b^2} = 1")

# --- Coordenadas Polares ---
with st.expander("9. Coordenadas Polares"):
    st.subheader("Definición")
    st.markdown("""
    El sistema de **coordenadas polares** es una forma alternativa de representar puntos en un plano. En lugar de usar coordenadas cartesianas $(x, y)$, se utiliza una distancia desde el origen (el **radio r**) y un ángulo desde un eje de referencia (el **ángulo θ**).
    - **r**: La distancia desde el polo (origen) al punto.
    - **θ**: El ángulo, medido en sentido antihorario desde el eje polar (equivalente al eje x positivo).
    """)

    st.subheader("Conversión de Cartesianas a Polares")
    st.markdown("Dado un punto $(x, y)$:")
    st.latex(r"r = \sqrt{x^2 + y^2}")
    st.latex(r"\theta = \arctan\left(\frac{y}{x}\right)")

    st.subheader("Conversión de Polares a Cartesianas")
    st.markdown("Dado un punto $(r, \theta)$:")
    st.latex(r"x = r \cdot \cos(\theta)")
    st.latex(r"y = r \cdot \sin(\theta)")

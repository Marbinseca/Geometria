import numpy as np

def calculate_distance(p1: tuple, p2: tuple) -> float:
    """Calcula la distancia euclidiana entre dos puntos."""
    point1 = np.array(p1)
    point2 = np.array(p2)
    return np.linalg.norm(point2 - point1)

def calculate_slope(p1: tuple, p2: tuple) -> float:
    """Calcula la pendiente de la recta que une dos puntos."""
    delta_x = p2[0] - p1[0]
    if delta_x == 0:
        return np.inf  # Pendiente indefinida para rectas verticales
    return (p2[1] - p1[1]) / delta_x


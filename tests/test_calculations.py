import pytest
import numpy as np
from utils.calculations import calculate_distance, calculate_slope

def test_calculate_distance():
    """Prueba la función de cálculo de distancia con casos conocidos."""
    assert calculate_distance((0, 0), (3, 4)) == 5.0
    assert calculate_distance((-1, 2), (2, 6)) == 5.0
    assert calculate_distance((0, 0), (0, 0)) == 0.0
    # Usamos approx para manejar la imprecisión de los flotantes
    assert calculate_distance((1, 1), (2, 2)) == pytest.approx(np.sqrt(2))

def test_calculate_slope():
    """Prueba la función de cálculo de pendiente."""
    assert calculate_slope((0, 0), (2, 2)) == 1.0
    assert calculate_slope((0, 0), (1, 3)) == 3.0
    assert calculate_slope((1, 5), (3, 9)) == 2.0
    assert calculate_slope((5, 2), (5, 10)) == np.inf # Recta vertical
    assert calculate_slope((2, 5), (10, 5)) == 0.0   # Recta horizontal


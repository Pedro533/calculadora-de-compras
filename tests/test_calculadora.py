"""
Tests de la calculadora eléctrica.

Ejecutar con:
    python -m pytest

Cada función de calculadora.py debería tener al menos un test acá.
"""

from calculadora import (
    calcular_tension,
    calcular_corriente,
    calcular_resistencia,
    calcular_potencia,
    resistencias_serie,
)


# ----- Ley de Ohm -----

def test_tension():
    # 2 A circulando por 6 Ω -> 12 V
    assert calcular_tension(2, 6) == 12


def test_corriente():
    # 12 V sobre 4 Ω -> 3 A
    assert calcular_corriente(12, 4) == 3


def test_resistencia():
    # 220 V con 2 A -> 110 Ω
    assert calcular_resistencia(220, 2) == 110


# ----- Potencia -----

def test_potencia():
    # 12 V y 5 A -> 60 W
    assert calcular_potencia(12, 5) == 60


# ----- Resistencias -----

def test_resistencias_serie():
    # 100 + 220 + 330 = 650 Ω
    assert resistencias_serie([100, 220, 330]) == 650


def test_resistencias_serie_una_sola():
    # Una sola resistencia: el equivalente es ella misma
    assert resistencias_serie([470]) == 470

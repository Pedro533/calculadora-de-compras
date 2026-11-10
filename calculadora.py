"""
Calculadora eléctrica
=====================

Funciones para resolver cálculos básicos de circuitos eléctricos.

Unidades que usa todo el módulo:
    tensión     -> volts   (V)
    corriente   -> amperes (A)
    resistencia -> ohms    (Ω)
    potencia    -> watts   (W)
"""


# ---------------------------------------------------------------
# Ley de Ohm
# ---------------------------------------------------------------

def calcular_tension(corriente, resistencia):
    """Ley de Ohm: V = I x R. Devuelve la tensión en volts."""
    return corriente * resistencia


def calcular_corriente(tension, resistencia):
    """Ley de Ohm: I = V / R. Devuelve la corriente en amperes."""
    return tension / resistencia


def calcular_resistencia(tension, corriente):
    """Ley de Ohm: R = V / I. Devuelve la resistencia en ohms."""
    return tension / corriente


# ---------------------------------------------------------------
# Potencia
# ---------------------------------------------------------------

def calcular_potencia(tension, corriente):
    """Potencia eléctrica: P = V x I. Devuelve la potencia en watts."""
    return tension * corriente


# ---------------------------------------------------------------
# Asociación de resistencias
# ---------------------------------------------------------------

def resistencias_serie(resistencias):
    """
    Resistencia equivalente en serie: Rt = R1 + R2 + R3 + ...

    Recibe una lista de valores en ohms, por ejemplo [100, 220, 330].
    """
    total = 0
    for r in resistencias:
        total = total + r
    return total


def resistencias_paralelo(resistencias):
    """
    Resistencia equivalente en paralelo: 1/Rt = 1/R1 + 1/R2 + 1/R3 + ...

    Recibe una lista de valores en ohms, por ejemplo [100, 100].
    """
    suma_inversas = 0
    for r in resistencias:
        suma_inversas = suma_inversas + 1 / r
    return suma_inversas

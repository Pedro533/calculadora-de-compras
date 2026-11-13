"""
Tests de la calculadora de compras.

Ejecutar con:
    python -m pytest

Cada función de calculadora.py debería tener al menos un test acá.
"""

from calculadora import (
    sumar_compras,
    agregar_iva,
    dividir_cuenta,
    calcular_vuelto,
)


# ----- Sumar compras -----

def test_sumar_compras():
    # $100 + $250 + $50 = $400
    assert sumar_compras([100, 250, 50]) == 400


def test_sumar_compras_un_solo_producto():
    # Si compro una sola cosa, el total es su precio
    assert sumar_compras([780]) == 780


# ----- IVA -----

def test_agregar_iva():
    # $1000 + 21% de IVA = $1210
    assert round(agregar_iva(1000), 2) == 1210


# ----- Dividir la cuenta -----

def test_dividir_cuenta():
    # $12000 entre 4 amigos = $3000 cada uno
    assert dividir_cuenta(12000, 4) == 3000


# ----- Vuelto -----

def test_calcular_vuelto():
    # Total $750, paga con $1000 -> vuelto $250
    assert calcular_vuelto(750, 1000) == 250


def test_calcular_vuelto_justo():
    # Paga justo -> no hay vuelto
    assert calcular_vuelto(500, 500) == 0


def test_dividir_cuenta_ok():
    # Test para asegurar que la división normal sigue funcionando
    assert dividir_cuenta(1000, 2) == 500
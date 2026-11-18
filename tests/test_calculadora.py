"""
Tests de la calculadora de compras.

Ejecutar con:
    python -m pytest

Cada función de calculadora.py debería tener al menos un test acá.
"""
import pytest

from calculadora import (
    sumar_compras,
    aplicar_descuento,
    agregar_iva,
    dividir_cuenta,
    calcular_vuelto,
    pesos_a_dolares,
    dolares_a_pesos,
    calcular_cuotas,
)

# ----- Sumar compras -----

def test_sumar_compras():
    # $100 + $250 + $50 = $400
    assert sumar_compras([100, 250, 50]) == 400


def test_sumar_compras_un_solo_producto():
    # Si compro una sola cosa, el total es su precio
    assert sumar_compras([780]) == 780


# ----- Descuentos -----

def test_aplicar_descuento_del_50_por_ciento():
    # $1000 con 50% de descuento = $500
    assert aplicar_descuento(1000, 50) == 500


def test_aplicar_descuento_del_10_por_ciento():
    # $2000 con 10% de descuento = $1800
    assert aplicar_descuento(2000, 10) == 1800


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

# ----- Conversor de moneda -----

def test_pesos_a_dolares_cotizacion_1000():
    # $50000 con cotización 1000 = US$ 50
    assert pesos_a_dolares(50000, 1000) == 50


def test_pesos_a_dolares_cotizacion_1200():
    # $15000 con cotización 1200 = US$ 12.50
    assert pesos_a_dolares(15000, 1200) == 12.50


def test_dolares_a_pesos_cotizacion_1000():
    # US$ 20 con cotización 1000 = $20000
    assert dolares_a_pesos(20, 1000) == 20000


def test_dolares_a_pesos_con_decimales():
    # US$ 12.5 con cotización 1200 = $15000
    assert dolares_a_pesos(12.5, 1200) == 15000

def test_pesos_a_dolares_cotizacion_cero():
    with pytest.raises(ValueError):
        pesos_a_dolares(10000, 0)


def test_dolares_a_pesos_cotizacion_cero():
    with pytest.raises(ValueError):
        dolares_a_pesos(10, 0)

# ----- Calcular cuotas -----

def test_calcular_cuotas_sin_interes():
    # $12000 en 3 cuotas sin interés = $4000 cada cuota
    assert calcular_cuotas(12000, 3, 0) == 4000


def test_calcular_cuotas_con_interes_del_10():
    # $12000 en 6 cuotas con 10% de interés = $2200 cada cuota
    assert calcular_cuotas(12000, 6, 10) == 2200


def test_calcular_cuotas_con_interes_del_20():
    # $9000 en 3 cuotas con 20% de interés = $3600 cada cuota
    assert calcular_cuotas(9000, 3, 20) == 3600


def test_calcular_cuotas_cero_debe_generar_error():
    # No se puede dividir el precio en cero cuotas
    with pytest.raises(
        ValueError,
        match="La cantidad de cuotas debe ser mayor que cero"
    ):
        calcular_cuotas(1000, 0, 10)


def test_calcular_cuotas_decimales_debe_generar_error():
    # La cantidad de cuotas debe ser un número entero
    with pytest.raises(
        ValueError,
        match="La cantidad de cuotas debe ser un número entero"
    ):
        calcular_cuotas(1000, 2.5, 10)


# ----- IVA -----

def test_agregar_iva_otro_caso():
    # $500 + 21% de IVA = $605
    assert round(agregar_iva(500), 2) == 605


# ----- Dividir la cuenta -----

def test_dividir_cuenta_otro_caso():
    # $10000 entre 5 personas = $2000 cada una
    assert dividir_cuenta(10000, 5) == 2000


# ----- Vuelto -----

def test_calcular_vuelto_otro_caso():
    # Total $1500, paga con $2000 -> vuelto $500
    assert calcular_vuelto(1500, 2000) == 500

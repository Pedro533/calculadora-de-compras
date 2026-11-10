"""
Calculadora de compras
======================

Funciones para hacer cuentas de todos los días:
sumar compras, descuentos, IVA, dividir la cuenta y calcular el vuelto.

Todos los precios están en pesos ($).
"""


def sumar_compras(precios):
    """
    Suma el precio de todos los productos comprados.

    Recibe una lista de precios, por ejemplo [100, 250, 50].
    """
    total = 0
    for precio in precios:
        total = total + precio
    return total


def aplicar_descuento(precio, porcentaje):
    """
    Devuelve el precio final después de aplicar un descuento.

    porcentaje: el descuento en %, por ejemplo 10 para un 10% de descuento.
    """
    return precio - porcentaje


def agregar_iva(precio):
    """Devuelve el precio con el IVA (21%) incluido."""
    return precio * 1.21


def dividir_cuenta(total, personas):
    """Divide el total de la cuenta en partes iguales entre las personas."""
    return total / personas


def calcular_vuelto(total, pagado):
    """Devuelve cuánto vuelto hay que dar: lo que pagó el cliente menos el total."""
    return pagado - total

"""
Menú de la calculadora de compras.

Ejecutar con:
    python main.py
"""

from calculadora import (
    sumar_compras,
    aplicar_descuento,
    agregar_iva,
    dividir_cuenta,
    calcular_vuelto,
    calcular_cuotas,
)


def pedir_numero(mensaje):
    """Pide un número al usuario y lo devuelve como float."""
    texto = input(mensaje)
    return float(texto)


def pedir_lista(mensaje):
    """Pide varios números separados por coma y los devuelve en una lista."""
    texto = input(mensaje)
    valores = []
    for parte in texto.split(","):
        valores.append(float(parte))
    return valores


def mostrar_menu():
    print()
    print("===== CALCULADORA DE COMPRAS =====")
    print("1. Sumar compras")
    print("2. Aplicar un descuento")
    print("3. Agregar IVA (21%)")
    print("4. Dividir la cuenta entre amigos")
    print("5. Calcular el vuelto")
    print("6. Calcular cuotas")
    print("0. Salir")


def main():
    while True:
        mostrar_menu()
        opcion = input("Elegí una opción: ")

        if opcion == "1":
            precios = pedir_lista("Precios separados por coma ($): ")
            print(f"Total = ${sumar_compras(precios):.2f}")

        elif opcion == "2":
            precio = pedir_numero("Precio ($): ")
            porcentaje = pedir_numero("Descuento (%): ")
            print(f"Precio con descuento = ${aplicar_descuento(precio, porcentaje):.2f}")

        elif opcion == "3":
            precio = pedir_numero("Precio sin IVA ($): ")
            print(f"Precio con IVA = ${agregar_iva(precio):.2f}")

        elif opcion == "4":
            total = pedir_numero("Total de la cuenta ($): ")
            personas = pedir_numero("Cantidad de personas: ")
            print(f"Paga cada uno = ${dividir_cuenta(total, personas):.2f}")

        elif opcion == "5":
            total = pedir_numero("Total a pagar ($): ")
            pagado = pedir_numero("Con cuánto paga el cliente ($): ")
            print(f"Vuelto = ${calcular_vuelto(total, pagado):.2f}")

        elif opcion == "6":
            precio = pedir_numero("Precio de la compra ($): ")
            cuotas = pedir_numero("Cantidad de cuotas: ")
            interes = pedir_numero("Interés (%): ")
            valor_cuota = calcular_cuotas(precio, cuotas, interes)
            print(f"Valor de cada cuota = ${valor_cuota:.2f}")

        elif opcion == "0":
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida, probá de nuevo.")


# Esta línea hace que el menú arranque solo cuando ejecutamos "python main.py"
if __name__ == "__main__":
    main()

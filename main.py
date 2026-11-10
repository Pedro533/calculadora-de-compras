"""
Menú de la calculadora eléctrica.

Ejecutar con:
    python main.py
"""

from calculadora import (
    calcular_tension,
    calcular_corriente,
    calcular_resistencia,
    calcular_potencia,
    resistencias_serie,
    resistencias_paralelo,
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
    print("===== CALCULADORA ELÉCTRICA =====")
    print("1. Calcular tensión (V = I x R)")
    print("2. Calcular corriente (I = V / R)")
    print("3. Calcular resistencia (R = V / I)")
    print("4. Calcular potencia (P = V x I)")
    print("5. Resistencias en serie")
    print("6. Resistencias en paralelo")
    print("0. Salir")


def main():
    while True:
        mostrar_menu()
        opcion = input("Elegí una opción: ")

        if opcion == "1":
            i = pedir_numero("Corriente (A): ")
            r = pedir_numero("Resistencia (ohm): ")
            print(f"Tensión = {calcular_tension(i, r):.2f} V")

        elif opcion == "2":
            v = pedir_numero("Tensión (V): ")
            r = pedir_numero("Resistencia (ohm): ")
            print(f"Corriente = {calcular_corriente(v, r):.2f} A")

        elif opcion == "3":
            v = pedir_numero("Tensión (V): ")
            i = pedir_numero("Corriente (A): ")
            print(f"Resistencia = {calcular_resistencia(v, i):.2f} ohm")

        elif opcion == "4":
            v = pedir_numero("Tensión (V): ")
            i = pedir_numero("Corriente (A): ")
            print(f"Potencia = {calcular_potencia(v, i):.2f} W")

        elif opcion == "5":
            lista = pedir_lista("Resistencias separadas por coma (ohm): ")
            print(f"Resistencia equivalente = {resistencias_serie(lista):.2f} ohm")

        elif opcion == "6":
            lista = pedir_lista("Resistencias separadas por coma (ohm): ")
            print(f"Resistencia equivalente = {resistencias_paralelo(lista):.2f} ohm")

        elif opcion == "0":
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida, probá de nuevo.")


# Esta línea hace que el menú arranque solo cuando ejecutamos "python main.py"
if __name__ == "__main__":
    main()

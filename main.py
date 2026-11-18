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
    pesos_a_dolares,
    dolares_a_pesos,
    calcular_cuotas,
)

def pedir_numero(mensaje):
    """Pide un número al usuario y lo devuelve como float. Valida que no sea negativo."""
    while True:
        texto = input(mensaje)
        try:
            numero = float(texto)
        except ValueError:
            print("Eso no es un número, probá de nuevo.")
            continue
        
        if numero < 0:
            print("El valor no puede ser negativo.")
            continue
            
        return numero


def pedir_lista(mensaje):
    """Pide varios números separados por coma. Valida que sean números y no negativos."""
    while True:
        texto = input(mensaje)
        try:
            valores = []
            es_valido = True
            for parte in texto.split(","):
                numero = float(parte.strip())
                if numero < 0:
                    print("El valor no puede ser negativo.")
                    es_valido = False
                    break # Cortamos el bucle for
                
                valores.append(numero)
            
            if es_valido:
                return valores
            
        except ValueError:
            print("Eso no es un número, probá de nuevo.")




def mostrar_menu():
    print()
    print("===== CALCULADORA DE COMPRAS =====")
    print("1. Sumar compras")
    print("2. Aplicar un descuento")
    print("3. Agregar IVA (21%)")
    print("4. Dividir la cuenta entre amigos")
    print("5. Calcular el vuelto")
    print("6. Calcular cuotas")
    print("7. Convertir pesos a dólares")
    print("8. Convertir dólares a pesos")
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
            while True:
                porcentaje = pedir_numero("Descuento (%): ")
                if porcentaje >= 100:
                    print("El descuento no puede ser mayor o igual al 100%. Probá de nuevo.")
                    continue
                break
            print(f"Precio con descuento = ${aplicar_descuento(precio, porcentaje):.2f}")
        


        elif opcion == "3":
            precio = pedir_numero("Precio sin IVA ($): ")
            print(f"Precio con IVA = ${agregar_iva(precio):.2f}")


        elif opcion == "4":
            total = pedir_numero("Total de la cuenta ($): ")
            while True:
                personas = pedir_numero("Cantidad de personas: ")
                if personas <= 0:
                    print("Tiene que haber al menos una persona.")
                    continue
                if personas != int(personas):
                    print("La cantidad de personas debe ser un número entero. Probá de nuevo.")
                    continue
                break
            
            print(f"Paga cada uno = ${dividir_cuenta(total, int(personas)):.2f}")

        elif opcion == "5":
            total = pedir_numero("Total a pagar ($): ")
            while True:
                pagado = pedir_numero("Con cuánto paga el cliente ($): ")
                if pagado < total:
                    print("El importe es insuficiente. Por favor, ingrese un monto mayor o igual al total.")
                    continue
                break
            print(f"Vuelto = ${calcular_vuelto(total, pagado):.2f}")
        
        

        elif opcion == "6":
            precio = pedir_numero("Precio de la compra ($): ")
            cuotas = pedir_numero("Cantidad de cuotas: ")

            if cuotas != int(cuotas):
                print("Error: La cantidad de cuotas debe ser un número entero.")
                continue

            cuotas = int(cuotas)
            interes = pedir_numero("Interés (%): ")

            try:
                valor_cuota = calcular_cuotas(precio, cuotas, interes)
                print(f"Valor de cada cuota = ${valor_cuota:.2f}")
            except ValueError as error:
                print(f"Error: {error}")

        elif opcion == "7":
            pesos = pedir_numero("Cantidad en pesos ($): ")
            cotizacion = pedir_numero("Cotización del día (pesos por 1 dólar): ")
            try:
                print(f"Resultado = US${pesos_a_dolares(pesos, cotizacion):.2f}")
            except ValueError as error:
                print(f"Error: {error}")

        elif opcion == "8":
            dolares = pedir_numero("Cantidad en dólares (US$): ")
            cotizacion = pedir_numero("Cotización del día (pesos por 1 dólar): ")
            try:
                print(f"Resultado = ${dolares_a_pesos(dolares, cotizacion):.2f}")
            except ValueError as error:
                print(f"Error: {error}")

        elif opcion == "0":
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida, probá de nuevo.")


# Esta línea hace que el menú arranque solo cuando ejecutamos "python main.py"
if __name__ == "__main__":
    main()

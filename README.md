# 🛒 Calculadora de Compras

Calculadora de consola, escrita en Python, para hacer las cuentas de todos los días: sumar lo que compraste, aplicar descuentos, agregar el IVA, dividir la cuenta con amigos y calcular el vuelto.

Es un proyecto abierto: **cualquiera puede proponer mejoras** haciendo un fork y enviando un Pull Request. Antes de contribuir, leé la [guía de contribución](CONTRIBUTING.md).

## Funciones disponibles

| Opción | Qué hace | Ejemplo |
|---|---|---|
| 1 | Sumar compras | $100, $250, $50 → $400 |
| 2 | Aplicar un descuento | $1000 con 10% → $900 |
| 3 | Agregar IVA (21%) | $1000 → $1210 |
| 4 | Dividir la cuenta entre amigos | $12000 entre 4 → $3000 cada uno (valida que no sea 0) | 
| 5 | Calcular el vuelto | Total $750, paga con $1000 → $250 |

*Nota: El sistema valida que el usuario ingrese números y no letras, y que los valores no sean negativos.*

## Requisitos

- [Python 3.10](https://www.python.org/downloads/) o superior
- [Git](https://git-scm.com/)

## Cómo usarla

```bash
git clone https://github.com/Pedro533/calculadora-de-compras.git
cd calculadora-de-compras
python main.py
```

Ejemplo de uso:

```
===== CALCULADORA DE COMPRAS =====
1. Sumar compras
...
Elegí una opción: 4
Total de la cuenta ($): 12000
Cantidad de personas: 4
Paga cada uno = $3000.00
```

## Cómo correr los tests

Los tests verifican que cada cuenta dé el resultado correcto.

```bash
pip install -r requirements.txt
python -m pytest
```

Si todo está bien vas a ver algo como `6 passed`.

## Estructura del proyecto

```
calculadora-de-compras/
├── calculadora.py        # Funciones que hacen las cuentas
├── main.py               # Menú para el usuario
├── tests/
│   └── test_calculadora.py   # Tests automáticos
├── CONTRIBUTING.md       # Cómo contribuir
├── LICENSE               # Licencia MIT
└── requirements.txt      # Dependencias (pytest)
```

## Cómo contribuir

1. Buscá un Issue abierto o creá uno nuevo.
2. Hacé un **fork** del repositorio.
3. Trabajá en una **rama** nueva.
4. Enviá un **Pull Request**.

Todo el detalle está en [CONTRIBUTING.md](CONTRIBUTING.md).

## Licencia

Este proyecto se distribuye bajo la [licencia MIT](LICENSE).

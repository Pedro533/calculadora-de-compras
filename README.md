# ⚡ Calculadora Eléctrica

Calculadora de consola, escrita en Python, para resolver cálculos básicos de circuitos eléctricos.

Es un proyecto abierto: **cualquiera puede proponer mejoras** haciendo un fork y enviando un Pull Request. Antes de contribuir, leé la [guía de contribución](CONTRIBUTING.md).

## Funciones disponibles

| Opción | Cálculo | Fórmula |
|---|---|---|
| 1 | Tensión | V = I × R |
| 2 | Corriente | I = V / R |
| 3 | Resistencia | R = V / I |
| 4 | Potencia | P = V × I |
| 5 | Resistencias en serie | Rt = R1 + R2 + … |
| 6 | Resistencias en paralelo | 1/Rt = 1/R1 + 1/R2 + … |

## Requisitos

- [Python 3.10](https://www.python.org/downloads/) o superior
- [Git](https://git-scm.com/)

## Cómo usarla

```bash
git clone https://github.com/Pedro533/calculadora-electrica.git
cd calculadora-electrica
python main.py
```

Ejemplo de uso:

```
===== CALCULADORA ELÉCTRICA =====
1. Calcular tensión (V = I x R)
...
Elegí una opción: 1
Corriente (A): 2
Resistencia (ohm): 6
Tensión = 12.00 V
```

## Cómo correr los tests

Los tests verifican que cada cálculo dé el resultado correcto.

```bash
pip install -r requirements.txt
python -m pytest
```

Si todo está bien vas a ver algo como `6 passed`.

## Estructura del proyecto

```
calculadora-electrica/
├── calculadora.py        # Funciones de cálculo
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

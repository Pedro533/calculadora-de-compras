# Guía de contribución

¡Gracias por querer mejorar la Calculadora Eléctrica! Este documento explica cómo trabajamos.

## Roles

| Rol | Quiénes | Qué hacen |
|---|---|---|
| **Maintainers** (Equipo QA) | Colaboradores de este repositorio | Revisan Pull Requests, escriben tests, reportan bugs, aprueban y hacen el merge |
| **Contributors** (Equipo DEV) | Trabajan desde un fork | Programan las mejoras y envían Pull Requests |

## Reglas del proyecto

1. **Nadie hace push directo a `main`.** Todo cambio entra por Pull Request.
2. **Cada Pull Request resuelve un solo Issue.**
3. **Toda función nueva lleva su test** en `tests/test_calculadora.py`.
4. **Los tests tienen que pasar** antes de pedir revisión.
5. **Un PR se mergea solo con la aprobación de un maintainer**, y nunca lo aprueba quien lo escribió.

## Flujo de trabajo para contributors

### 1. Fork y clone (una sola vez)

1. En GitHub, botón **Fork** (arriba a la derecha).
2. Clonar **tu fork**:

```bash
git clone https://github.com/TU-USUARIO/calculadora-electrica.git
cd calculadora-electrica
```

3. Conectar con el repositorio original (**upstream**):

```bash
git remote add upstream https://github.com/Pedro533/calculadora-electrica.git
git remote -v
```

Vas a ver dos remotos: `origin` (tu fork) y `upstream` (el original).

### 2. Antes de empezar cada tarea: sincronizar

```bash
git checkout main
git fetch upstream
git merge upstream/main
git push origin main
```

### 3. Crear una rama para el Issue

Nombre de la rama: `tipo/numero-descripcion-corta`

```bash
git checkout -b feature/3-capacitores
```

| Tipo | Para qué |
|---|---|
| `feature/` | Función nueva |
| `fix/` | Corrección de un bug |
| `test/` | Tests nuevos |
| `docs/` | Cambios en documentación |

### 4. Programar y commitear

```bash
git add calculadora.py tests/test_calculadora.py
git commit -m "Agrega cálculo de capacitores en serie"
```

**Mensajes de commit:**
- En tiempo presente: "Agrega…", "Corrige…", "Actualiza…"
- Cortos y que expliquen **qué** cambió
- Un commit = un cambio lógico (no todo junto)

| ✅ Bien | ❌ Mal |
|---|---|
| `Agrega validación de valores negativos` | `cambios` |
| `Corrige fórmula de resistencias en paralelo` | `arreglé cosas` |
| `Agrega test para caída de tensión` | `asdf` |

### 5. Correr los tests

```bash
python -m pytest
```

### 6. Subir la rama y abrir el Pull Request

```bash
git push origin feature/3-capacitores
```

En GitHub: **Compare & pull request** → completar la plantilla → **Create pull request**.

En la descripción escribí `Closes #3` (con el número del Issue) para que se cierre solo al mergear.

### 7. Si te piden cambios

Hacé los cambios en la **misma rama**, commiteá y volvé a hacer push. El PR se actualiza solo.

## Flujo de trabajo para maintainers

1. Revisar el código en la pestaña **Files changed**.
2. Bajar la rama y probarla:

```bash
git fetch origin pull/NUMERO/head:revision-NUMERO
git checkout revision-NUMERO
python -m pytest
python main.py
```

3. Dejar comentarios en líneas concretas del código.
4. Elegir: **Comment**, **Request changes** o **Approve**.
5. Si está aprobado: **Merge pull request** y borrar la rama.

## Reportar un bug

Abrí un Issue con la plantilla **Reporte de bug** y contá:
- Qué hiciste (valores de entrada)
- Qué esperabas que pasara
- Qué pasó en realidad

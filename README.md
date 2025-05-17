# Sistema de Gestión de Evaluaciones

# Miembros del Grupo 4: [ADRIANA BETANCOURTH, LISSETTE DANIELA MERO, WILLIAM VELEZ BARRE]

## Descripción del Proyecto

Este sistema modela diferentes tipos de evaluaciones académicas (Examen, Trabajo, Presentacion) utilizando los principios de la Programación Orientada a Objetos (POO) en Python.  Se define una clase base abstracta `Evaluacion` con atributos comunes y un método abstracto `calcular_nota()`. Las subclases `Examen`, `Trabajo`, y `Presentacion` (implementadas aquí Examen y Trabajo)  heredan de `Evaluacion` y proporcionan sus propias implementaciones del método `calcular_nota()` para calcular las notas de las evaluaciones específicas. [cite: 1, 2, 3, 4, 5]

## Instrucciones para Ejecutar el Sistema

1.  Asegúrate de tener Python 3.x instalado.
2.  Instala Pycharm (recomendado).
3.  Clona el repositorio de GitHub.
4.  Abre el proyecto en Pycharm.
5.  Ejecuta el archivo `src/main.py`.

## Descripción de Clases

* **Evaluacion (clase base abstracta):**
    * Atributos: `nombre` (str), `fecha` (date), `puntaje` (float).
    * Métodos: `__init__()`, `calcular_nota()` (abstracto), getters y setters (como propiedades).
    * Propósito: Define la estructura común para todas las evaluaciones. No se puede instanciar directamente.
* **Examen (subclase de Evaluacion):**
    * Atributos adicionales: `preguntas` (int), `respuestas_correctas` (int).
    * Métodos: `__init__()`, `calcular_nota()` (sobrescrito), getters y setters.
    * Propósito: Representa

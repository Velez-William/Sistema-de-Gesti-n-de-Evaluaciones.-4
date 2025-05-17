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
 
      ![image](https://github.com/user-attachments/assets/a07c466d-7e31-47c7-a95c-3fb2deb94b15)


* **Examen (subclase de Evaluacion):**
  subclase1
  Herencia: Examen hereda de Evaluacion usando class Examen(Evaluacion):. __init__: El constructor de Examen llama al constructor de la superclase (super().__init__(nombre, fecha, puntaje)) y luego inicializa los atributos 
  específicos de Examen (_preguntas, _respuestas_correctas).
   Getters/Setters: Se implementan los getters y setters para los atributos propios de la clase Examen.
   calcular_nota() (Polimorfismo): Este método está sobrescrito (redefinido) para proporcionar la lógica de cálculo de la nota específica para un examen. 
    __str__ method: The __str__ method is implemented to provide a string representation of the Examen object.
    Pruebas Unitarias: Incluye pruebas para crear un Examen, mostrar su información y calcular la nota. 

  ![image](https://github.com/user-attachments/assets/e1a6ef68-c4ce-45d4-be85-29ea3e9f320a)

  subclase 2
  Herencia: Trabajo también hereda de Evaluacion. __init__: Constructor similar a Examen, inicializando atributos de la superclase y los propios (_calificacion_tecnica, _calificacion_presentacion).
  Getters/Setters: Getters y setters para los atributos de Trabajo.
  calcular_nota() (Polimorfismo): Implementación específica para calcular la nota de un trabajo, con una ponderación de la calificación técnica y de presentación. 
   __str__ method: The __str__ method is implemented to provide a string representation of the Trabajo object.
   Pruebas Unitarias: Pruebas para crear un Trabajo y calcular su nota. 
  
![image](https://github.com/user-attachments/assets/41518fb3-1161-4dc3-8e07-207cd261c87b)

* **main.py 
     *Importaciones: Importa las clases necesarias (Evaluacion, Examen, Trabajo) y date.
      *Instanciación: Crea instancias de Examen y Trabajo.
      *Uso de Métodos: Llama a los métodos calcular_nota() y otros para demostrar su funcionamiento.
      *Polimorfismo (Ejemplo): El ejemplo final (opcional) muestra cómo se puede tratar a los objetos de las subclases (Examen, Trabajo) como objetos de la superclase (Evaluacion) y cómo el método calcular_nota() se 
       comporta
     *manera diferente según el tipo real del objeto. 

   ![image](https://github.com/user-attachments/assets/6725ca23-732c-48af-b1e3-bdd3f97b3ee7)


    * Atributos adicionales: `preguntas` (int), `respuestas_correctas` (int).
    * Métodos: `__init__()`, `calcular_nota()` (sobrescrito), getters y setters.
    * Propósito: Representa
      

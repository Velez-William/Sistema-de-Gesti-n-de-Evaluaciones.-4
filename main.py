# src/main.py
# Miembros del Grupo 4: [ADRIANA BETANCOURTH, LISSETTE DANIELA MERO, WILLIAM VELEZ BARRE]

"""
Propósito: Clase principal para instanciar y probar las clases Evaluacion, Examen y Trabajo.
"""


from src.clase_base import Evaluacion
from src.subclase1 import Examen
from src.subclase2 import Trabajo
from datetime import date

if __name__ == '__main__':
    # Crear instancias de las subclases
    fecha_examen = date(2025, 5, 25)
    examen1 = Examen("Parcial 1", fecha_examen, 100, 20, 18)

    fecha_trabajo = date(2025, 5, 5)
    trabajo1 = Trabajo("Proyecto", fecha_trabajo, 100, 85, 92)

    # Mostrar información de las evaluaciones
    print(examen1)
    print(trabajo1)

    # Calcular y mostrar las notas
    print(f"Nota del {examen1.nombre}: {examen1.calcular_nota()}")
    print(f"Nota del {trabajo1.nombre}: {trabajo1.calcular_nota()}")

    # Modificar y mostrar la nota actualizada del examen
    examen1.respuestas_correctas = 15
    print(f"Nota actualizada del {examen1.nombre}: {examen1.calcular_nota()}")

    # Ejemplo de polimorfismo (opcional, pero ilustrativo)
    evaluaciones = [examen1, trabajo1]  # Lista de objetos de tipo Evaluacion (o sus subclases)
    print("\n--- Demostración de Polimorfismo ---")
    for evaluacion in evaluaciones:
        print(f"Evaluación: {evaluacion.nombre}, Nota: {evaluacion.calcular_nota()}")
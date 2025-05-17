# src/subclase1.py
# Miembros del Grupo 4: [ADRIANA BETANCOURTH, LISSETTE DANIELA MERO, WILLIAM VELEZ BARRE]

"""
Propósito: Define la clase Examen, una subclase de Evaluacion, con una forma específica de calcular la nota.
"""

from src.clase_base import Evaluacion  # Importa la clase base
from datetime import date

class Examen(Evaluacion):
    """
    Clase que representa un examen, un tipo de evaluación.
    """

    def __init__(self, nombre: str, fecha: date, puntaje: float, preguntas: int, respuestas_correctas: int):
        """
        Constructor de la clase Examen.

        Args:
            nombre (str): El nombre del examen.
            fecha (date): La fecha del examen.
            puntaje (float): El puntaje máximo del examen.
            preguntas (int): El número total de preguntas en el examen.
            respuestas_correctas (int): El número de respuestas correctas del estudiante.
        """
        super().__init__(nombre, fecha, puntaje)  # Llama al constructor de la superclase
        self._preguntas = preguntas
        self._respuestas_correctas = respuestas_correctas

    # Getters y Setters para nuevos atributos (preguntas, respuestas_correctas)
    @property
    def preguntas(self):
        return self._preguntas

    @preguntas.setter
    def preguntas(self, nuevas_preguntas):
        self._preguntas = nuevas_preguntas

    @property
    def respuestas_correctas(self):
        return self._respuestas_correctas

    @respuestas_correctas.setter
    def respuestas_correctas(self, nuevas_respuestas_correctas):
        self._respuestas_correctas = nuevas_respuestas_correctas

    def calcular_nota(self):
        """
        Calcula la nota del examen basado en el número de respuestas correctas.
        (Ejemplo: Regla de tres simple_)
        """
        if self._preguntas > 0:
            return (self._respuestas_correctas / self._preguntas) * self._puntaje
        else:
            return 0  # Evita la división por cero

    def __str__(self):
        return f"Examen--> {self.__dict__.__str__()}"


# Pruebas unitarias (ejemplos)
if __name__ == '__main__':
    fecha_examen = date(2025, 5, 25)
    examen = Examen("Parcial 1", fecha_examen, 10, 20, 18)
    print(examen)
    print(f"Nota del examen: {examen.calcular_nota()}")

    examen.respuestas_correctas = 15
    print(f"Nota actualizada: {examen.calcular_nota()}")
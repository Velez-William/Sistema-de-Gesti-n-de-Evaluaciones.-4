# src/subclase2.py
# Miembros del Grupo 4: [ADRIANA BETANCOURTH, LISSETTE DANIELA MERO, WILLIAM VELEZ BARRE]

"""
Propósito: Define la clase Trabajo, una subclase de Evaluacion, con su propia forma de calcular la nota.
"""

from src.clase_base import Evaluacion
from datetime import date

class Trabajo(Evaluacion):
    """
    Clase que representa un trabajo práctico, otro tipo de evaluación.
    """

    def __init__(self, nombre: str, fecha: date, puntaje: float, calificacion_tecnica: float, calificacion_presentacion: float):
        """
        Constructor de la clase Trabajo.

        Args:
            nombre (str): El nombre del trabajo.
            fecha (date): La fecha de entrega del trabajo.
            puntaje (float): El puntaje máximo del trabajo.
            calificacion_tecnica (float): Calificación de la parte técnica del trabajo.
            calificacion_presentacion (float): Calificación de la presentación del trabajo.
        """
        super().__init__(nombre, fecha, puntaje)
        self._calificacion_tecnica = calificacion_tecnica
        self._calificacion_presentacion = calificacion_presentacion

    # Getters y Setters
    @property
    def calificacion_tecnica(self):
        return self._calificacion_tecnica

    @calificacion_tecnica.setter
    def calificacion_tecnica(self, nueva_calificacion_tecnica):
        self._calificacion_tecnica = nueva_calificacion_tecnica

    @property
    def calificacion_presentacion(self):
        return self._calificacion_presentacion

    @calificacion_presentacion.setter
    def calificacion_presentacion(self, nueva_calificacion_presentacion):
        self._calificacion_presentacion = nueva_calificacion_presentacion

    def calcular_nota(self):
        """
        Calcula la nota del trabajo ponderando la calificación técnica y la de presentación.
        (Ejemplo: 60% técnica, 40% presentación)
        """
        return (0.6 * self._calificacion_tecnica + 0.4 * self._calificacion_presentacion) * self._puntaje / 100

    def __str__(self):
          return f"Trabajo--> {self.__dict__.__str__()}"


# Pruebas unitarias (ejemplos)
if __name__ == '__main__':
    fecha_trabajo = date(2025, 5, 25)
    trabajo = Trabajo("PROYECTO", fecha_trabajo, 100, 85, 92)
    print(trabajo)
    print(f"Nota del trabajo: {trabajo.calcular_nota()}")

    trabajo.calificacion_tecnica = 78
    print(f"Nota actualizada: {trabajo.calcular_nota()}")
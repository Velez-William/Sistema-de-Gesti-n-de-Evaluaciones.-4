# src/clase_base.py
# Miembros del Grupo 4: [ADRIANA BETANCOURTH, LISSETTE DANIELA MERO, WILLIAM VELEZ BARRE]

"""
Propósito: Define la clase base abstracta Evaluacion para el sistema de gestión de evaluaciones.
"""

from abc import ABC, abstractmethod
from datetime import date  # Importa la clase date

class Evaluacion(ABC):
    """
    Clase abstracta que representa una evaluación académica.
    """

    def __init__(self, nombre: str, fecha: date, puntaje: float):
        """
        Constructor de la clase Evaluacion.

        Args:
            nombre (str): El nombre de la evaluación.
            fecha (date): La fecha de la evaluación.
            puntaje (float): El puntaje máximo de la evaluación.
        """
        self._nombre = nombre  # Encapsulamiento: Atributos protegidos
        self._fecha = fecha
        self._puntaje = puntaje

    # Getters y Setters como propiedades
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    @property
    def fecha(self):
        return self._fecha

    @fecha.setter
    def fecha(self, nueva_fecha):
        self._fecha = nueva_fecha

    @property
    def puntaje(self):
        return self._puntaje

    @puntaje.setter
    def puntaje(self, nuevo_puntaje):
        if nuevo_puntaje > 0:
          self._puntaje = nuevo_puntaje
        else:
          print("El puntaje no puede ser negativo")

    @abstractmethod
    def calcular_nota(self):
        """
        Método abstracto para calcular la nota de la evaluación.
        Este método debe ser implementado por las subclases.
        """
        pass

    def __str__(self):
        return f"Evaluación--> {self.__dict__.__str__()}"


# Pruebas unitarias (ejemplos)
if __name__ == '__main__':
    #  Crear una instancia de Evaluacion directamente generará un error ya que_ es abstracta
    # evaluacion_base = Evaluacion("Prueba", "2025-05-25", 100)
    print("Clase base de Evaluacion definida correctamente")
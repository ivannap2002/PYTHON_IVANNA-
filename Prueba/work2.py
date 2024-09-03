from abc import ABC, abstractmethod

class Persona(ABC):
    """Clase que representa una persona"""
    @abstractmethod
    def __init__(self, cedula, nombre, apellido):
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido

    @abstractmethod
    def __str__(self):
        return "%s: %s, %s" % (str(self.cedula), self.apellido, self.nombre)

class Alumno(Persona):
    """Clase que representa a un alumno"""
    def __init__(self, cedula, nombre, apellido, carrera):
        # Llamamos al constructor de Persona
        super().__init__(cedula, nombre, apellido)
        # Agregamos el nuevo atributo
        self.carrera = carrera

    def __str__(self):
        # Retorna todos los atributos de la clase
        return "Cédula: %s, Nombre: %s %s, Carrera: %s" % (self.cedula, self.nombre, self.apellido, self.carrera)

if __name__ == "__main__":
    # Crear un objeto del tipo Alumno
    alumno = Alumno("5.044.017", "Ivanna", "Peña", "Ingeniería")
    # Imprimir sus datos
    print(alumno)

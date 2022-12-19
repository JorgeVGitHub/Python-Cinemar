from db import base

class Usuario:
    def __init__(self, nombre):
        self.__nombre = nombre

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nuevo):
        self.__nombre = nuevo

    def crear(self):
        base.crear_db()

    def insertar(self):
        base.insertar_usuario(self.__nombre)

class Pelicula:
    def __init__(self, nombre):
        self.__nombre = nombre

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nuevo):
        self.__nombre = nuevo

class Sala:
    def __init__(self, nombre):
        self.__nombre = nombre

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nuevo):
        self.__nombre = nuevo

class Reserva:
    def __init__(self, usuario, fecha, pelicula, sala):
        self.usuario = usuario
        self.fecha = fecha
        self.pelicula = pelicula
        self.sala = sala


def hola():
    return "hola"
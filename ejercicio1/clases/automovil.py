from clases.vehiculo import Vehiculo
from utils.rendimientos import r_auto

class Automovil(Vehiculo):
    def __init__(self, id_vehiculo, marca, modelo, año_fabricacion, puertas):
        super().__init__(id_vehiculo, marca, modelo, año_fabricacion)
        self.__puertas = puertas

    def descripcion(self):
        return "AUTOMOVIL\n" + super().descripcion()
    
    def calcular_consumo(self, km):
        consumo = km / (r_auto - (self.__puertas - 2) * 0.5)
        return round(consumo, 2)
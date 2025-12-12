from clases.vehiculo import Vehiculo
from utils.rendimientos import r_camion

class Camion(Vehiculo):
    def __init__(self, id_vehiculo, marca, modelo, año_fabricacion, capacidad_carga):
        super().__init__(id_vehiculo, marca, modelo, año_fabricacion)
        self.__capacidad_carga = capacidad_carga

    def descripcion(self):
        return "CAMION\n" + super().descripcion() 
    
    def calcular_consumo(self, km):
        consumo = km / (r_camion - (self.__capacidad_carga * 0.2))
        return round(consumo, 2)
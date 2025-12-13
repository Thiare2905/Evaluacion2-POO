from clases.vehiculo import Vehiculo
from utils.rendimientos import r_auto

# Clase Automovil que hereda de Vehiculo
class Automovil(Vehiculo):
    def __init__(self, id_vehiculo, marca, modelo, año_fabricacion, puertas):
        super().__init__(id_vehiculo, marca, modelo, año_fabricacion)
        self.__puertas = puertas    # Se agrega una nueva variable 

    # Método que muestra la descripción 
    def descripcion(self):
        return "AUTOMOVIL\n" + super().descripcion()
    
    # Método que calcula el consumo estimado del vehiculo
    def calcular_consumo(self, km):
        # calculo: base (r_auto=12) menos 0.5 por puerta extra sobre las 2 estandar
        consumo = km / (r_auto - (self.__puertas - 2) * 0.5)
        return round(consumo, 2)
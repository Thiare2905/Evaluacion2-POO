from clases.vehiculo import Vehiculo
from utils.rendimientos import r_camion

# Clase Camion que hereda de Vehiculo
class Camion(Vehiculo):
    def __init__(self, id_vehiculo, marca, modelo, año_fabricacion, capacidad_carga):
        super().__init__(id_vehiculo, marca, modelo, año_fabricacion)
        self.__capacidad_carga = capacidad_carga     # Se agrega una nueva variable 

    # Método que muestra la descripción
    def descripcion(self):
        return "CAMION\n" + super().descripcion() 
    
    # Método que calcula el consumo estimado del vehiculo
    def calcular_consumo(self, km):
        # calculo: base(r_camoin=5) menos 0.2 de penalizacion por cada tonelada de carga
        consumo = km / (r_camion - (self.__capacidad_carga * 0.2))
        return round(consumo, 2)
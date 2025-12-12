from clases.vehiculo import Vehiculo
from utils.rendimientos import r_moto

class Motocicleta(Vehiculo):
    def __init__(self, id_vehiculo, marca, modelo, año_fabricacion, cilindrada):
        super().__init__(id_vehiculo, marca, modelo, año_fabricacion)
        self.__cilindrada = cilindrada

    def descripcion(self):
        return "MOTOCICLETA\n" + super().descripcion() 
    
    def calcular_consumo(self, km):
        consumo = km / (r_moto - (self.__cilindrada / 100) * 2)
        return round(consumo, 2)
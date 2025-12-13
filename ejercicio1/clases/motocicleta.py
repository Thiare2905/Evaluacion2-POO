from clases.vehiculo import Vehiculo
from utils.rendimientos import r_moto

# Clase Motocicleta que hereda de Vehiculo
class Motocicleta(Vehiculo):
    def __init__(self, id_vehiculo, marca, modelo, año_fabricacion, cilindrada):
        super().__init__(id_vehiculo, marca, modelo, año_fabricacion)
        self.__cilindrada = cilindrada   # Se agrega una nueva variable 

    # Método que muestra la descripción
    def descripcion(self):
        return "MOTOCICLETA\n" + super().descripcion() 
    
    # Método que calcula el consumo estimado del vehiculo
    def calcular_consumo(self, km):
        # calculo: la base(r_moto=30) menos 2 de penalizacion por cada 100cc de cilindrada
        consumo = km / (r_moto - (self.__cilindrada / 100) * 2)
        return round(consumo, 2)
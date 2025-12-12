class Vehiculo:
    def __init__(self, id_vehiculo, marca, modelo, año_fabricacion):
        self.__id_vehiculo = id_vehiculo
        self.__marca = marca
        self.__modelo = modelo
        self.__año_fabricacion = año_fabricacion

    def descripcion(self):
        return f"Patente: {self.__id_vehiculo} | Marca: {self.__marca} | Modelo: {self.__modelo} | Año: {self.__año_fabricacion}"
    
    def calcular_consumo(self, km):
        pass

    def get_id(self):
        return self.__id_vehiculo
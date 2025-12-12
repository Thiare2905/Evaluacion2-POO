from clases.vehiculo import Vehiculo

class Flota:
    def __init__(self):
        self.vehiculos = []

    def agregar(self, vehiculo:Vehiculo):
        for v in self.vehiculos:
            if v.get_id() == vehiculo.get_id():
                return F"Ya existe este vehiculo ({vehiculo.get_id()})."
        self.vehiculos.append(vehiculo)
        return f"Vehiculo {vehiculo.get_id()} agregado."
    
    def eliminar(self, identificador):
        for v in self.vehiculos:
            if v.get_id() == identificador:
                self.vehiculos.remove(v)
                return f"Se eliminó el vehiculo {identificador}"
        return f"Vehiculo {identificador} no encontrado."
    
    def buscar(self, identificador):
        for v in self.vehiculos:
            if v.get_id() == identificador:
                print(v.descripcion())
                return v.calcular_consumo(150)
                
        return f"Vehiculo {identificador} no encontrado"
from clases.vehiculo import Vehiculo

# Clase Flota para gestionar vehiculos
class Flota:
    def __init__(self):
        self.vehiculos = [] # Se inicializa lista vacia para guardar los vehiculos

    # Método que agrega un nuevo vehiculo a la flota
    def agregar(self, vehiculo:Vehiculo):
        # ciclo que recorre la lista 
        for v in self.vehiculos:
            # Si ya está el vehiculo, se informa
            if v.get_id() == vehiculo.get_id():
                return F"Ya existe este vehiculo ({vehiculo.get_id()})."
        # se agrea a la lista e informa se que agregó
        self.vehiculos.append(vehiculo)
        return f"Vehiculo {vehiculo.get_id()} agregado."
    
    # Método que elimina un vehiculo
    def eliminar(self, identificador):
        # ciclo que recorre la lista 
        for v in self.vehiculos:
            # si encuentra el vehiculo se elimina y se informa que esta eliminado
            if v.get_id() == identificador:
                self.vehiculos.remove(v)
                return f"Se eliminó el vehiculo {identificador}"
        # de lo contrario se informa que no fue encontrado
        return f"Vehiculo {identificador} no encontrado."
    
    # Método para buscar un vehiculo
    def buscar(self, identificador):
        # ciclo que recorre la lista 
        for v in self.vehiculos:
            # si se encuentra
            if v.get_id() == identificador:
                # muestra la información del vehiculo y su consumo estimado
                print(v.descripcion())
                return v.calcular_consumo(150)
        # de lo contradio se informa que no se encontró
        return f"Vehiculo {identificador} no encontrado."
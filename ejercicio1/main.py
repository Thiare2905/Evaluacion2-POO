from clases.automovil import Automovil
from clases.motocicleta import Motocicleta
from clases.camion import Camion
from clases.flota import Flota

# variable que guardala el consumo total
total_consumo = 0.0

# Se instancia la flota
flota = Flota()
# Se instancian vehiculos de clase Automovil, Motocicleta y Camion
auto = Automovil("PK-LS-20", "MG", "mg6", 2021, 4)
moto = Motocicleta("JX-452", "Honda", "CB500X", 2022, 471)
camion = Camion("CAM-999", "Volvo", "FH16", 2018, 12)
# Vehiculo que repite identificador
camion2 = Camion("CAM-999", "Volvo", "FH", 2019, 12)

# Se agregan los distintos vehiculos
print("--- AGREGACIÓN DE VEHICULOS ---")
print(flota.agregar(auto))
print(flota.agregar(moto))
print(flota.agregar(camion))
print(flota.agregar(camion2))

# Se llama al método que elimina un vehiculo
# print(flota.eliminar("JX-452"))

# Se llama al método que busca un vehiculo
print("\n--- BUSQUEDA DE VEHICULO ---")
print(flota.buscar("CAM-999"))

print("\n--- FLOTA DE VEHICULOS ---")
# Se recorre la flota 
for v in flota.vehiculos:
    # Se llama al método para mostrar la descripcion del vehiculo
    print(v.descripcion())

print("\n--- CONSUMO ESTIMADO ---")
# Se recorre la flota
for v in flota.vehiculos:
    # type(v).__name__ para mostrar el nombre de Clase 
    # Se llama la funcion que calula el consumo estimado con 150 km
    print(f"{type(v).__name__} ({v.get_id()}): {v.calcular_consumo(150)} litros")
    # Se va sumando los consumos
    total_consumo += v.calcular_consumo(150)
# Se muestra el Consumo total de la flota
print(f"** Consumo total de la flota: {round(total_consumo, 2)}")
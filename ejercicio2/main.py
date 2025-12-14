from clases.empresa import Empresa
from clases.gerente import Gerente
from clases.vendedor import Vendedor
from clases.practicante import Practicante

empresa = Empresa()

gerente = Gerente("Moises Muñoz Correa", "17.889.222-0", 1300000, 500000, False)
vendedor = Vendedor("Valentina Soto Vera", "13.234.554-9", 700000, 150)
practicante = Practicante("Nicolas Berrios Morales", "18.998.321-1", 0, 120)
gerente2 = Gerente("Sofia Alvarado Garrido", "12.009.2255-0", 1250000, 600000)
vendedor2 = Vendedor("Esteban Solis Mora", "11.774.999-9", 870000, 135, False)
practicante2 = Practicante("Karen Olea Mancilla", "20.665.123-4", 0, 200)

print("--- AGREGACIÓN DE EMPLEADOS ---")
print(empresa.agregar(gerente))
print(empresa.agregar(vendedor))
print(empresa.agregar(practicante))
print(empresa.agregar(gerente2))
print(empresa.agregar(vendedor2))
print(empresa.agregar(practicante2))

print("\n--- lISTADO DE EMPLEADOS ---")
empresa.filtrar_activos()

print("\n--- REPORTE ---")
print(empresa.gasto_total())
from clases.banco import Banco
from clases.cuenta_corriente import Cuenta_Corriente
from clases.cuenta_ahorro import Cuenta_Ahorro

# Crear instancia del banco
banco = Banco()

# Crear cuentas bancarias
c_ahorro = Cuenta_Ahorro("001", "Rodrigo Perez", 50000)
c_ahorro2 = Cuenta_Ahorro("002", "Maria Tiznado", 47000)
c_corriente = Cuenta_Corriente("003", "Ana Macaya", 29000)
c_corriente2 = Cuenta_Corriente("004", "Hector Miralles", 1500)

# Agregar cuentas al banco y mostrar resultados
print(" --- NUEVAS CUENTAS ---")
print(banco.agregar_cuenta(c_ahorro))
print(banco.agregar_cuenta(c_ahorro2))
print(banco.agregar_cuenta(c_corriente))
print(banco.agregar_cuenta(c_corriente2))

# Se realizan depositos
print("\n --- DEPOSITOS ---")
print(c_ahorro.depositar(3000))
print(c_corriente.depositar(8990))

# Se realizan retiros
print("\n --- RETIROS ---")
print(c_corriente2.retirar(3000))
print(c_corriente.retirar(200))

# Se agrega interes a las cuentas de ahorro
print("\n --- INTERES ---")
print(c_ahorro2.agregar_interes())

# Mostrar info de las cuentas
print("\n --- CUENTAS DEL BANCO ---")
for c in banco.cuentas:
    print(c.info_cuenta())

# Mostrar historial de una cuenta
print("\n --- HISTORIAL ---")
banco.buscar("003")

# Mostrar saldo total administrado por el banco
print("\n --- SALDO ADMINISTRADO ---")
print(banco.saldo_total())


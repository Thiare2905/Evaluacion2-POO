from clases.banco import Banco
from clases.cuenta_corriente import Cuenta_Corriente
from clases.cuenta_ahorro import Cuenta_Ahorro

banco = Banco()

c_ahorro = Cuenta_Ahorro("001", "Rodrigo Perez", 50000)
c_ahorro2 = Cuenta_Ahorro("002", "Maria Tiznado", 47000)
c_corriente = Cuenta_Corriente("003", "Ana Macaya", 29000)
c_corriente2 = Cuenta_Corriente("004", "Hector Miralles", 1500)

print(" --- NUEVAS CUENTAS ---")
print(banco.agregar_cuenta(c_ahorro))
print(banco.agregar_cuenta(c_ahorro2))
print(banco.agregar_cuenta(c_corriente))
print(banco.agregar_cuenta(c_corriente2))

print("\n --- DEPOSITOS ---")
print(c_ahorro.depositar(3000))
print(c_corriente.depositar(8990))

print("\n --- RETIROS ---")
print(c_corriente2.retirar(3000))
print(c_corriente.retirar(200))

print("\n --- INTERES ---")
print(c_ahorro2.agregar_interes())

print("\n --- CUENTAS DEL BANCO ---")
for c in banco.cuentas:
    print(c.info_cuenta())

print("\n --- HISTORIAL ---")
banco.buscar("003")

print("\n --- SALDO ADMINISTRADO ---")
print(banco.saldo_total())


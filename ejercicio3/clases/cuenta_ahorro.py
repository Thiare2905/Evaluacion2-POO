from clases.cuenta_bancaria import Cuenta_Bancaria

# Valor del porcentaje de interés para cuentas de ahorro
porcentaje_interes = 0.04

# Clase Cuenta_Ahorro (Hija de Cuenta_Bancaria)
class Cuenta_Ahorro(Cuenta_Bancaria):
    def __init__(self, num_cuenta, nombre_titular, saldo_actual, tipo_cuenta="Ahorro"):
        super().__init__(num_cuenta, nombre_titular, saldo_actual, tipo_cuenta)

    # Métodos depositar y agregar_interes
    def depositar(self, monto):
        return super().depositar(monto)
    
    def agregar_interes(self):
        interes = self.get_saldo() * porcentaje_interes
        return super().agregar_interes(interes)
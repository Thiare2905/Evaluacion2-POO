from clases.cuenta_bancaria import Cuenta_Bancaria

porcentaje_interes = 0.04

class Cuenta_Ahorro(Cuenta_Bancaria):
    def __init__(self, num_cuenta, nombre_titular, saldo_actual, tipo_cuenta="Ahorro"):
        super().__init__(num_cuenta, nombre_titular, saldo_actual, tipo_cuenta)

    def depositar(self, monto):
        return super().depositar(monto)
    
    def agregar_interes(self):
        interes = self.get_saldo() * porcentaje_interes
        return super().agregar_interes(interes)
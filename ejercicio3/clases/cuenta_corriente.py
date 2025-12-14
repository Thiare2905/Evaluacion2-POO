from clases.cuenta_bancaria import Cuenta_Bancaria

sobre_giro = -1500

class Cuenta_Corriente(Cuenta_Bancaria):
    def __init__(self, num_cuenta, nombre_titular, saldo_actual, tipo_cuenta="Corriente"):
        super().__init__(num_cuenta, nombre_titular, saldo_actual, tipo_cuenta)
    
    def depositar(self, monto):
        return super().depositar(monto)
    
    def retirar(self, monto):
        if self.get_saldo() - monto < sobre_giro:
            return "No puede retirar el monto excede la linea de credito."
        return super().retirar(monto)
        
    

"""
saldo  monto resultado
3000 - 1500 = 1500
1500 - 1500 = 0
1000 - 1500 = -500
1000 - 2500 = -1500
"""
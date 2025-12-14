from clases.cuenta_bancaria import Cuenta_Bancaria

# Definición del límite de sobregiro
sobre_giro = -1500

# Clase Cuenta_Corriente (Hija de Cuenta_Bancaria)
class Cuenta_Corriente(Cuenta_Bancaria):
    def __init__(self, num_cuenta, nombre_titular, saldo_actual, tipo_cuenta="Corriente"):
        super().__init__(num_cuenta, nombre_titular, saldo_actual, tipo_cuenta)
    
    # Métodos depositar y retirar
    def depositar(self, monto):
        return super().depositar(monto)
    
    def retirar(self, monto):
        if self.get_saldo() - monto < sobre_giro:
            return "No puede retirar el monto excede la linea de credito."
        return super().retirar(monto)
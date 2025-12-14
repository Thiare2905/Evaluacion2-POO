from clases.cuenta_bancaria import Cuenta_Bancaria

# Clase Banco
class Banco:
    def __init__(self):
        self.cuentas = [] # Lista para almacenar las cuentas bancarias

    # Método para agregar una cuenta bancaria
    def agregar_cuenta(self, cuenta:Cuenta_Bancaria):
        for c in self.cuentas:
            if c.get_numero() == cuenta.get_numero():
                return f"{cuenta.get_nombre()}esta cuenta ya existe."
        self.cuentas.append(cuenta)
        return f"Se agrego con exito {cuenta.get_nombre()}."
    
    # Método para buscar una cuenta bancaria por su número
    def buscar(self, num_cuenta):
        for c in self.cuentas:
            if c.get_numero() == num_cuenta:
                return c.historial()

    # Método para calcular el saldo total de todas las cuentas bancarias
    def saldo_total(self):
        sum = 0
        for c in self.cuentas:
            sum += c.get_saldo()
        return f"Saldo: {sum}"
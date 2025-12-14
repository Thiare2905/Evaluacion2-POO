# Clase Cuenta_Bancaria
class Cuenta_Bancaria:
    def __init__(self, num_cuenta, nombre_titular, saldo_actual, tipo_cuenta):
        self.__num_cuenta = num_cuenta
        self.__nombre_titular = nombre_titular
        self.__saldo_actual = saldo_actual
        self.__tipo_cuenta = tipo_cuenta
        self.__movimientos = []

    # Método depositar
    def depositar(self, monto):
        if monto <= 0:
            return "El monto debe ser mayor a 0."    
        self.__saldo_actual += monto
        self.movimiento(f"DEPOSITO - {monto}")
        return f"{self.__nombre_titular} su saldo es: {self.__saldo_actual}"
    
    # Método retirar
    def retirar(self, monto):
        self.movimiento(f"RETIRO - {monto}")
        self.__saldo_actual -= monto
        return f"{self.__nombre_titular} su saldo es: {self.__saldo_actual}"

    # Método info_cuenta
    def info_cuenta(self):
        return f"Titular: {self.__nombre_titular} - Cuenta: {self.__tipo_cuenta} - Saldo: {self.__saldo_actual}"
    
    # Método historial
    def historial(self):
        for m in self.__movimientos:
            print(m)

    # Método movimiento (privado)
    def movimiento(self, mensaje):
        self.__movimientos.append(mensaje)
    
    # Método agregar_interes 
    def agregar_interes(self, interes):
        self.__saldo_actual += interes
        self.movimiento(f"INTERÉS: {interes}")
        return f"Con el interes su saldo es: {self.__saldo_actual}"

    # Getters
    def get_saldo(self):
        return self.__saldo_actual
    
    def get_numero(self):
        return self.__num_cuenta
    
    def get_nombre(self):
        return self.__nombre_titular
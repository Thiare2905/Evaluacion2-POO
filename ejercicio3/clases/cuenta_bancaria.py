class Cuenta_Bancaria:
    def __init__(self, num_cuenta, nombre_titular, saldo_actual, tipo_cuenta):
        self.__num_cuenta = num_cuenta
        self.__nombre_titular = nombre_titular
        self.__saldo_actual = saldo_actual
        self.__tipo_cuenta = tipo_cuenta
        self.__movimientos = []

    def depositar(self, monto):
        if monto <= 0:
            return "El monto debe ser mayor a 0."    
        self.__saldo_actual += monto
        self.movimiento(f"DEPOSITO - {monto}")
        return f"{self.__nombre_titular} su saldo es: {self.__saldo_actual}"
    
    def retirar(self, monto):
        self.movimiento(f"RETIRO - {monto}")
        self.__saldo_actual -= monto
        return f"{self.__nombre_titular} su saldo es: {self.__saldo_actual}"

    def info_cuenta(self):
        return f"Titular: {self.__nombre_titular} - Cuenta: {self.__tipo_cuenta} - Saldo: {self.__saldo_actual}"
    
    def historial(self):
        for m in self.__movimientos:
            print(m)

    def movimiento(self, mensaje):
        self.__movimientos.append(mensaje)

    def agregar_interes(self, interes):
        self.__saldo_actual += interes
        self.movimiento(f"INTERÉS: {interes}")
        return f"Con el interes su saldo es: {self.__saldo_actual}"

    def get_saldo(self):
        return self.__saldo_actual
    
    def get_numero(self):
        return self.__num_cuenta
    
    def get_nombre(self):
        return self.__nombre_titular
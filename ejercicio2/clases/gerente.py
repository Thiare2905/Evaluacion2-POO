from clases.empleado import Empleado

class Gerente(Empleado):
    def __init__(self, nombre, rut, sueldo_base, bono, activo=True):
        super().__init__(nombre, rut, sueldo_base, activo)
        self.__bono = bono

    def remuneracion_mensual(self):
        return super().remuneracion_mensual() + self.__bono
    
    def resumen(self):
        return super().resumen() + f"|Remuneración mensual: {self.remuneracion_mensual()}"
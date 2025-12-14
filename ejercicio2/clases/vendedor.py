from clases.empleado import Empleado

comision = 0.15

class Vendedor(Empleado):
    def __init__(self, nombre, rut, sueldo_base, ventas, activo=True):
        super().__init__(nombre, rut, sueldo_base, activo)
        self.__ventas = ventas

    def remuneracion_mensual(self):
        return super().remuneracion_mensual() + (comision * self.__ventas)
    
    def resumen(self):
        return super().resumen() + f"|Remuneración mensual: {self.remuneracion_mensual()}"
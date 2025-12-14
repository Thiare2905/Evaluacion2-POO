from clases.empleado import Empleado

valor_hora = 5000

class Practicante(Empleado):
    def __init__(self, nombre, rut, sueldo_base, horas_trabajadas, activo=True):
        super().__init__(nombre, rut, sueldo_base, activo)
        self.__horas_trabajadas = horas_trabajadas

    def remuneracion_mensual(self):
        return self.__horas_trabajadas * valor_hora
    
    def resumen(self):
        return super().resumen() + f"|Remuneración mensual: {self.remuneracion_mensual()}"
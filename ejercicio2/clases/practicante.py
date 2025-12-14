from clases.empleado import Empleado

# Valor por hora para practicantes
valor_hora = 5000

# Clase Practicante (Hija de Empleado)
class Practicante(Empleado):
    def __init__(self, nombre, rut, sueldo_base, horas_trabajadas, activo=True):
        super().__init__(nombre, rut, sueldo_base, activo)
        self.__horas_trabajadas = horas_trabajadas # Horas trabajadas por el practicante

    # Método para obtener la remuneración mensual
    def remuneracion_mensual(self):
        return self.__horas_trabajadas * valor_hora # Cálculo del sueldo según horas trabajadas
    
    # Método resumen de la información del practicante
    def resumen(self):
        return super().resumen() + f"|Remuneración mensual: {self.remuneracion_mensual()}"
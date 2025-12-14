from clases.empleado import Empleado

# Clase Gerente (Hija de Empleado)
class Gerente(Empleado):
    def __init__(self, nombre, rut, sueldo_base, bono, activo=True):
        super().__init__(nombre, rut, sueldo_base, activo)
        self.__bono = bono # Bono adicional para el gerente

    # Método para obtener la remuneración mensual
    def remuneracion_mensual(self):
        return super().remuneracion_mensual() + self.__bono # Suma del sueldo base y el bono
    
    # Método resumen de la información del gerente
    def resumen(self):
        return super().resumen() + f"|Remuneración mensual: {self.remuneracion_mensual()}"
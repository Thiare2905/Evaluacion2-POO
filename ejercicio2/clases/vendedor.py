from clases.empleado import Empleado

# Valor de comisión para vendedores
comision = 0.15

# Clase Vendedor (Hija de Empleado)
class Vendedor(Empleado):
    def __init__(self, nombre, rut, sueldo_base, ventas, activo=True):
        super().__init__(nombre, rut, sueldo_base, activo)
        self.__ventas = ventas # Monto total de ventas realizadas por el vendedor

    # Método para obtener la remuneración mensual
    def remuneracion_mensual(self):
        return super().remuneracion_mensual() + (comision * self.__ventas) # Suma del sueldo base y la comisión por ventas
    
    # Método resumen de la información del vendedor
    def resumen(self):
        return super().resumen() + f"|Remuneración mensual: {self.remuneracion_mensual()}"
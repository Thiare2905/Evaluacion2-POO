# Clase Empleado (Padre) 
class Empleado:
    def __init__(self, nombre, rut, sueldo_base, activo=True):
        self.__nombre = nombre
        self.__rut = rut
        self.__sueldo_base = sueldo_base
        self.__activo = activo

    # Método resumen de la información del empleado
    def resumen(self):
        return f"Nombre: {self.__nombre}|Rut: {self.__rut}|Sueldo base: {self.__sueldo_base}"
    
    # Método para obtener la remuneración mensual
    def remuneracion_mensual(self):
        return self.__sueldo_base
    
    # Getters
    def get_rut(self):
        return self.__rut
    
    def get_nombre(self):
        return self.__nombre
    
    def get_activo(self):
        return self.__activo
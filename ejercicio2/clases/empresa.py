from clases.empleado import Empleado

class Empresa:
    def __init__(self):
        self.empleados = []

    def agregar(self, empleado:Empleado):
        for e in self.empleados:
            if e.get_rut() == empleado.get_rut():
                return f"El empleado '{e.get_nombre()}' ya está registrado."
        self.empleados.append(empleado)
        return f"Se añadió el empleado '{empleado.get_nombre()}'."
    
    def filtrar_activos(self):
        print(" - ACTIVOS -")
        for e in self.empleados:
            if e.get_activo() == True:
                print(e.resumen())
        print(" - INACTIVOS -")
        for e in self.empleados:
            if e.get_activo() != True:
                print(e.resumen())

    def gasto_total(self):
        total = 0
        for e in self.empleados:
            if e.get_activo() == True:
                print(f"Tipo: {type(e).__name__} | Nombre: {e.get_nombre()} | {e.remuneracion_mensual()}")
                total += e.remuneracion_mensual() 
        return f"** Gasto total mensual: {total}"        
from clases.producto import Producto

# Recargo por licencia comercial
recargo = 0.20

# Clase Producto Digital que hereda de Producto
class Producto_Digital(Producto):
    def __init__(self, cod_prodcuto, nombre, precio_un, stock, licencia_comercial):
        super().__init__(cod_prodcuto, nombre, precio_un, stock)
        self.__licencia_comercial = licencia_comercial

    # Método para calcular el precio final con recargo si aplicable
    def calculo_final(self, cantidad):
        total = super().calculo_final(cantidad)
        if self.__licencia_comercial == True:
            return total + (total * recargo)
        return total
    
    # Método para mostrar detalles del producto
    def detalles(self):
        return "Tipo: Digital | " + super().detalles() + f"Total: {self.calculo_final(self.get_stock())}"
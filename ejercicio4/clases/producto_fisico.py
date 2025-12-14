from clases.producto import Producto

# Costos de envío según peso
liviano = 3000
estandar = 6000
pesado = 10000

# Clase Producto Físico que hereda de Producto
class Producto_Fisico(Producto):
    def __init__(self, cod_prodcuto, nombre, precio_un, stock, peso):
        super().__init__(cod_prodcuto, nombre, precio_un, stock)
        self.__peso = peso

    # Método para calcular el precio final con costo de envío
    def calculo_final(self, cantidad):
        total = super().calculo_final(cantidad)
        if self.__peso == "liviano":
            return total + liviano
        if self.__peso == "estandar":
            return total + estandar
        if self.__peso == "pesado":
            return total + pesado
        return "Peso incorrecto."
    
    # Método para mostrar detalles del producto
    def detalles(self):
        return "Tipo: Fisico | " + super().detalles() + f"Total: {self.calculo_final(self.get_stock())}"
    

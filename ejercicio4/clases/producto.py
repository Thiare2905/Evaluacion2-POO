# Clase Producto base
class Producto:
    def __init__(self, cod_prodcuto, nombre, precio_un, stock):
        self.__cod_producto = cod_prodcuto
        self.__nombre = nombre
        self.__precio_un = precio_un
        self.__stock = stock

    # Método para calcular el precio final
    def calculo_final(self, cantidad):
        if cantidad <= 0:
            return "La cantidad debe ser mayor a 0."
        if cantidad > self.__stock:
            return "La cantidad excede el stock."
        return self.__precio_un * cantidad

    # Método para mostrar detalles del producto
    def detalles(self):
        return f"Nombre: {self.__nombre} | Cantidad: {self.__stock} | "

    # Getters 
    def get_stock(self):
        return self.__stock
    
    def get_cod(self):
        return self.__cod_producto
    
    # Setter
    def descontar_stock(self, cantidad):
        self.__stock -= cantidad
from clases.producto import Producto
from clases.producto_digital import Producto_Digital
from clases.producto_fisico import Producto_Fisico

# Clase Carrito de compras
class Carrito:
    def __init__(self):
        self.productos = []

    # Método para agregar un producto al carrito
    def agregar(self, producto:Producto, cantidad):
        if cantidad > producto.get_stock():
            return "No hay stock suficiente."
        self.productos.append(producto)
        producto.descontar_stock(cantidad)
        return f"Se agregó el producto {producto.get_cod()}"
    
    # Método para eliminar un producto del carrito
    def eliminar(self, codigo):
        for p in self.productos:
            if p.get_cod() != codigo:
                return f"No se encontro el producto con el codigo {codigo}."
        self.productos.remove(p)
        return f"Producto eliminado {codigo}."
    
    # Método para mostrar el resumen de productos en el carrito
    def resumen(self):
        for p in self.productos:
            print(p.detalles())

    # Método para calcular el total del carrito
    def total_carrito(self):
        total = 0
        for p in self.productos:
            total += p.calculo_final(p.get_stock())
        return total
            
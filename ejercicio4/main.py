from clases.carrito import Carrito
from clases.producto_digital import Producto_Digital
from clases.producto_fisico import Producto_Fisico

# Crear carrito de compras
carrito = Carrito()

# Crear productos
p_digital = Producto_Digital("D01", "Curso Online", 20000, 10, True)
p_digital2 = Producto_Digital("D02", "Ebook", 10000, 50, False)
p_fisico = Producto_Fisico("F01", "Libro Python", 20000, 10, "liviano")
p_fisico2 = Producto_Fisico("F02", "Mochila", 35000, 12, "estandar")

# Agregar productos al carrito
print("-- SE AGREGAN PRODUCTOS --")
print(carrito.agregar(p_digital, 2))
print(carrito.agregar(p_digital2, 30))
print(carrito.agregar(p_fisico, 5))
print(carrito.agregar(p_fisico2, 9))

# Mostrar detalles de los productos en el carrito
print("\n-- DETALLES DE PRODUCTOS --")
carrito.resumen()

# Mostrar el total a pagar
total = 0
print("\n-- TOTAL A PAGAR --")
print(f"Total: {carrito.total_carrito()}")
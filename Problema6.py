class Producto:
    def __init__(self, nombre, precio, año):
        self.nombre = nombre
        self.precio = precio
        self.año = año

    def __str__(self):
        return f"Producto: {self.nombre}, Precio: S/.{self.precio}, Año: {self.año}"

class Catálogo:
    def __init__(self):
        ## Catálogo vacío.
        self.productos = []

    def agregar_producto(self, producto):
        #Agrega un producto al catálogo.
        self.productos.append(producto)

    def mostrar_productos(self):
        # Muestra todos los productos en el catálogo.
        if not self.productos:
            print("El catálogo está vacío.")
        else:
            for producto in self.productos:
                print(producto)

    def filtrar_por_año(self, año):
        #Muestra todos los productos que sean del año indicado
        productos_filtrados = [producto for producto in self.productos if producto.año == año]
        if not productos_filtrados:
            print(f"No se encontraron productos del año {año}.")
        else:
            print(f"Productos del año {año}:")
            for producto in productos_filtrados:
                print(producto)

    def filtrar_por_precio_maximo(self, precio_maximo):
        ## Muestra todos los productos cuyo precio sea menor o igual al precio máximo indicado.
        productos_filtrados = [producto for producto in self.productos if producto.precio <= precio_maximo]
        if not productos_filtrados:
            print(f"No se encontraron productos con un precio menor o igual a S/.{precio_maximo}.")
        else:
            print(f"Productos con un precio menor o igual a S/.{precio_maximo}:")
            for producto in productos_filtrados:
                print(producto)

def main():
    # Crear un catálogo
    catalogo = Catálogo()

    # Crear tres productos
    producto1 = Producto("Faro delantero", 100, 2021)
    producto2 = Producto("Parachoque", 400, 2018)
    producto3 = Producto("Estribo", 450, 2020)

    # Agregar los productos al catálogo
    catalogo.agregar_producto(producto1)
    catalogo.agregar_producto(producto2)
    catalogo.agregar_producto(producto3)

    # Mostrar todos los productos del catálogo
    print("Lista de todos los productos en el catálogo:")
    catalogo.mostrar_productos()

    # Filtrar productos por año
    print("\nFiltrar productos del año 2018:")
    catalogo.filtrar_por_año(2018)

    # Filtrar productos por precio máximo
    print("\nFiltrar productos con precio menor o igual a S/.430:")
    catalogo.filtrar_por_precio_maximo(430)

# Asegurarse de que el código se ejecute solo si es el script principal
if __name__ == '__main__':
    main()
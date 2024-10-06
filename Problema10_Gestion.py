from Problema10_Libro import Libro

class GestionBiblioteca:
    def __init__(self):
        self.libros = []  # Lista de libros vacía

    def agregar_libro(self, libro):
        self.libros.append(libro)  # Agrega un libro a la lista

    def listar_libros(self):
        if not self.libros:
            print("No hay libros en la biblioteca.")
        else:
            print("Lista de libros en la biblioteca:")
            for libro in self.libros:
                print(libro)  

    def buscar_por_titulo(self, titulo):
        encontrados = [libro for libro in self.libros if libro.titulo.lower() == titulo.lower()]
        if encontrados:
            print("Libros encontrados por título:")
            for libro in encontrados:
                print(libro)
        else:
            print("No se encontraron libros con ese título.")

    def buscar_por_autor(self, autor):
        encontrados = [libro for libro in self.libros if libro.autor.lower() == autor.lower()]
        if encontrados:
            print("Libros encontrados por autor:")
            for libro in encontrados:
                print(libro)
        else:
            print("No se encontraron libros de ese autor.")
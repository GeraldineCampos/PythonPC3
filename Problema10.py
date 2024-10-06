from Problema10_Gestion import GestionBiblioteca
from Problema10_Libro import Libro

def main():
    gestion = GestionBiblioteca()

    while True:
        print("\n--- Menú de Gestión de Biblioteca ---")
        print("1. Agregar un libro")
        print("2. Listar libros")
        print("3. Buscar libro por título")
        print("4. Buscar libro por autor")
        print("5. Salir")

        opcion = input("Seleccione una opción (1-5): ")

        if opcion == '1':
            titulo = input("Ingrese el título del libro: ")
            autor = input("Ingrese el autor del libro: ")
            isbn = input("Ingrese el ISBN del libro: ")
            libro = Libro(titulo, autor, isbn)
            gestion.agregar_libro(libro)
            print("Libro agregado con éxito.")

        elif opcion == '2':
            gestion.listar_libros()

        elif opcion == '3':
            titulo = input("Ingrese el título del libro a buscar: ")
            gestion.buscar_por_titulo(titulo)

        elif opcion == '4':
            autor = input("Ingrese el autor a buscar: ")
            gestion.buscar_por_autor(autor)

        elif opcion == '5':
            print("Saliendo del programa...")
            break

        else:
            print("Error: Opción no válida. Por favor seleccione una opción entre 1 y 5.")

if __name__ == '__main__':
    main()
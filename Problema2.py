def get_grades():
    
    while True:
        try:
            # Solicitar las calificaciones al usuario
            grades_input = input("Ingrese una lista de calificaciones separadas por comas: ")

            # Dividir la cadena ingresada en partes individuales
            grades_list = grades_input.split(",")

            # Convertir cada calificación en un entero
            grades = [int(grade.strip()) for grade in grades_list]

            return grades

        except ValueError:
            print("Error: Por favor, ingrese solo números enteros separados por comas. Inténtelo de nuevo.")

def main():
    # Obtener las calificaciones del usuario
    grades = get_grades()

    # Mostrar la lista de calificaciones obtenida
    print(f"Las calificaciones ingresadas son: {grades}")

if __name__ == '__main__':
    main()
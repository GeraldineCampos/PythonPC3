from Problema3 import CIRCULO
from Problema4 import RECTANGULO, CUADRADO

def es_numero_valido(valor):
    """Verifica si el valor es un número positivo."""
    try:
        numero = float(valor)
        return numero > 0  # Devuelve True si es positivo
    except ValueError:
        return False  # Devuelve False si no es un número

def main():
    while True:
        print("\nMenú:")
        print("1. Calcular el área de un círculo")
        print("2. Calcular el área de un rectángulo")
        print("3. Calcular el área de un cuadrado")
        print("4. Salir")

        opcion = input("Seleccione una opción (1-4): ")

        if opcion == '1':
            radio = input("Ingrese el radio del círculo: ")
            if es_numero_valido(radio):
                circulo = CIRCULO(float(radio))
                print(f"El área del círculo es: {circulo.area():.2f}")
            else:
                print("Error: El radio debe ser un número positivo.")

        elif opcion == '2':
            largo = input("Ingrese el largo del rectángulo: ")
            ancho = input("Ingrese el ancho del rectángulo: ")
            if es_numero_valido(largo) and es_numero_valido(ancho):
                rectangulo = RECTANGULO(float(largo), float(ancho))
                print(f"El área del rectángulo es: {rectangulo.area():.2f}")
            else:
                print("Error: El largo y el ancho deben ser números positivos.")

        elif opcion == '3':
            lado = input("Ingrese el lado del cuadrado: ")
            if es_numero_valido(lado):
                cuadrado = CUADRADO(float(lado))
                print(f"El área del cuadrado es: {cuadrado.area():.2f}")
            else:
                print("Error: El lado debe ser un número positivo.")

        elif opcion == '4':
            print("Saliendo del programa...")
            break

        else:
            print("Error: Opción no válida. Por favor seleccione una opción entre 1 y 4.")

if __name__ == '__main__':
    main()
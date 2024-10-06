import Problema8_Operaciones

def main():
    # Ejemplos de suma
    print("Suma de 9 y 5:", Problema8_Operaciones.suma(9, 5))
    print("Suma de '9' y 5:", Problema8_Operaciones.suma('9', 5))  # Tipo de dato no válido

    # Ejemplos de resta
    print("\nResta de 9 y 5:", Problema8_Operaciones.resta(9, 5))
    print("Resta de 9 y '5':", Problema8_Operaciones.resta(9, '5'))  # Tipo de dato no válido

    # Ejemplos de producto
    print("\nProducto de 9 y 5:", Problema8_Operaciones.producto(9, 5))
    print("Producto de 9 y '5':", Problema8_Operaciones.producto(9, '5'))  # Tipo de dato no válido

    # Ejemplos de división
    print("\nDivisión de 9 y 5:", Problema8_Operaciones.division(9, 5))
    print("División de 9 y 0:", Problema8_Operaciones.division(9, 0))  # División por cero
    print("División de 9 y '5':", Problema8_Operaciones.division(9, '5'))  # Tipo de dato no válido

if __name__ == '__main__':
    main()
class RECTANGULO:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho

    def area(self):
        return self.largo * self.ancho

class CUADRADO(RECTANGULO):
    def __init__(self, lado):
        super().__init__(lado, lado)

def main():
    # Crear un objeto de tipo RECTANGULO
    rectangulo = RECTANGULO(8, 5)  # Largo 8 y ancho 5

    # Crear un objeto de tipo CUADRADO
    cuadrado = CUADRADO(6)  # Cuadrado con lado de 6

    # Calcular y mostrar el área del rectángulo
    area_rectangulo = rectangulo.area()
    print(f"El área del rectángulo cuando el largo es {rectangulo.largo} y el ancho es {rectangulo.ancho} es: {area_rectangulo}")

    # Calcular y mostrar el área del cuadrado
    area_cuadrado = cuadrado.area()
    print(f"El área del cuadrado cuando el lado es {cuadrado.largo} es: {area_cuadrado}")

if __name__ == '__main__':
    main()
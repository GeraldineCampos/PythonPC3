import math

class CIRCULO:
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * (self.radio ** 2)

def main():
    # Crear dos objetos de tipo CIRCULO
    circulo1 = CIRCULO(7)  # Círculo con radio 7
    circulo2 = CIRCULO(9) # Círculo con radio 9

    # Calcular y mostrar el área de cada círculo
    area1 = circulo1.area()
    area2 = circulo2.area()

    print(f"El área del primer círculo cuando el radio es {circulo1.radio} es: {area1:.2f}")
    print(f"El área del segundo círculo cuando el radio es {circulo2.radio} es: {area2:.2f}")

if __name__ == '__main__':
    main()
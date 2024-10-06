import math

class Punto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def cuadrante(self):
        ## A qué cuadrante pertenece el punto
        if self.x == 0 and self.y == 0:
            return "El punto está en el origen"
        elif self.x == 0:
            return "El punto está sobre el eje Y"
        elif self.y == 0:
            return "El punto está sobre el eje X"
        elif self.x > 0 and self.y > 0:
            return "El punto está en el primer cuadrante"
        elif self.x < 0 and self.y > 0:
            return "El punto está en el segundo cuadrante"
        elif self.x < 0 and self.y < 0:
            return "El punto está en el tercer cuadrante"
        elif self.x > 0 and self.y < 0:
            return "El punto está en el cuarto cuadrante"

    def vector(self, otro):
        ## Calcula el vector resultante entre el punto actual y otro punto
        return Punto(otro.x - self.x, otro.y - self.y)

    def distancia(self, otro):
        ## Calcula la distancia entre el punto actual y otro punto
        return math.sqrt((otro.x - self.x) ** 2 + (otro.y - self.y) ** 2)

class Rectangulo:
    def __init__(self, punto_inicial=Punto(), punto_final=Punto()):
        ## Inicializa un rectangulo definido por dos puntos que forman su diagonal
        self.punto_inicial = punto_inicial
        self.punto_final = punto_final

    def base(self):
        ## Calculo de la base del rectángulo.
        return abs(self.punto_final.x - self.punto_inicial.x)

    def altura(self):
        ## Calculo de la altura del rectángulo
        return abs(self.punto_final.y - self.punto_inicial.y)

    def area(self):
        #Calculo del área del rectángulo
        return self.base() * self.altura()

def main():
    A = Punto(2, 3)
    B = Punto(5, 5)
    C = Punto(-3, -1)
    D = Punto(0, 0)

    print("Puntos creados:")
    print(f"A: {A}")
    print(f"B: {B}")
    print(f"C: {C}")
    print(f"D: {D}")

    # Consultar a qué cuadrante pertenecen los puntos A, C, y D
    print("\nCuadrantes:")
    print(f"A: {A.cuadrante()}")
    print(f"C: {C.cuadrante()}")
    print(f"D: {D.cuadrante()}")

    # Consultar los vectores AB y BA
    AB = A.vector(B)
    BA = B.vector(A)
    print("\nVectores:")
    print(f"Vector AB: {AB}")
    print(f"Vector BA: {BA}")

    # Consultar la distancia entre los puntos A y B
    distancia_AB = A.distancia(B)
    distancia_BA = B.distancia(A)
    print("\nDistancias:")
    print(f"Distancia entre A y B: {distancia_AB:.2f}")
    print(f"Distancia entre B y A: {distancia_BA:.2f}")

    # Determinar cuál de los puntos A, B, o C está más lejos del origen
    distancia_A = A.distancia(D)
    distancia_B = B.distancia(D)
    distancia_C = C.distancia(D)

    mas_lejos = max(distancia_A, distancia_B, distancia_C)
    if mas_lejos == distancia_A:
        print("\nEl punto A está más lejos del origen.")
    elif mas_lejos == distancia_B:
        print("\nEl punto B está más lejos del origen.")
    else:
        print("\nEl punto C está más lejos del origen.")

    # Crear un rectángulo utilizando los puntos A y B
    rectangulo = Rectangulo(A, B)

    # Consultar la base, altura y área del rectángulo
    print("\nRectángulo formado por los puntos A y B:")
    print(f"Base: {rectangulo.base()}")
    print(f"Altura: {rectangulo.altura()}")
    print(f"Área: {rectangulo.area()}")

if __name__ == '__main__':
    main()
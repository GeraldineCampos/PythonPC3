class Alumno:
    def __init__(self, nombre, numero_registro):
        self.nombre = nombre
        self.numero_registro = numero_registro
        self.edad = None
        self.nota = None

    def display(self):
        print(f"Nombre: {self.nombre}")
        print(f"Número de registro: {self.numero_registro}")
        if self.edad is not None:
            print(f"Edad: {self.edad}")
        if self.nota is not None:
            print(f"Nota: {self.nota}")

    def setAge(self, edad):
        self.edad = edad

    def setNota(self, nota):
        self.nota = nota

def main():
    alumno1 = Alumno("Geraldine Campos", "2024001")

    print("Información inicial del alumno:")
    alumno1.display()
    alumno1.setAge(23)  # Edad de 23 años
    alumno1.setNota(20) # Nota de 20
    print("\nInformación actualizada del alumno:")
    alumno1.display()

if __name__ == '__main__':
    main()
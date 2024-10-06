def obtener_fraccion():
    
    while True:
        try:
            fraccion = input("Por favor, ingrese una fracción en el formato X/Y: ")

            # Dividir la entrada en X e Y
            x_str, y_str = fraccion.split("/")
            x = int(x_str)
            y = int(y_str)

            # Verificar si Y es cero
            if y == 0:
                raise ZeroDivisionError("El denominador no puede ser cero.")

            # Verificar si X es mayor que Y
            if x > y:
                raise ValueError("El numerador no puede ser mayor que el denominador.")

            return x, y

        except ValueError:
            print("Error: Ingrese solo números enteros y asegúrese de que el numerador sea menor o igual al denominador.")
        except ZeroDivisionError:
            print("Error: El denominador no puede ser cero.")

def convertir_a_porcentaje(x, y):
    ## Para convertir la fracción X/Y a un porcentaje.
    return round((x / y) * 100)

def main():
    # Obtener la fracción del usuario
    x, y = obtener_fraccion()

    # Convertir la fracción a porcentaje
    porcentaje = convertir_a_porcentaje(x, y)

    # Determinar la salida
    if porcentaje <= 1:
        print("E")
    elif porcentaje >= 99:
        print("F")
    else:
        print(f"{porcentaje}%")

if __name__ == '__main__':
    main()
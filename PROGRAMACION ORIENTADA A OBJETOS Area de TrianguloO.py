# Clase que representa un triángulo
class Triangulo:
    # Constructor (__init__) que inicializa los atributos base y altura
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    # Método para calcular el área del triángulo
    def calcular_area(self):
        return (self.base * self.altura) / 2


# Función principal para manejar la interacción con el usuario
def main():
    try:
        # Solicita al usuario que ingrese los datos
        base = float(input("Ingresa la base del triángulo: "))
        altura = float(input("Ingresa la altura del triángulo: "))

        # Crea una instancia de la clase Triangulo (objeto)
        mi_triangulo = Triangulo(base, altura)

        # Calcula el área usando el método de la clase
        area = mi_triangulo.calcular_area()

        # Muestra el resultado
        print(f"El área del triángulo es: {area:.2f}")

    except ValueError:
        # En caso de que el usuario ingrese datos no numéricos
        print("Error: Solo se permiten números.")

# Punto de entrada del programa
if __name__ == "__main__":
    main()

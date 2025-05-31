# Función que calcula el área de un triángulo
def calcular_area(base, altura):
    return (base * altura) / 2

# Función principal
def main():
    print("=== Cálculo del área de un triángulo ===")
    
    # Solicita la base al usuario
    base = float(input("Ingresa la base: "))
    
    # Solicita la altura al usuario
    altura = float(input("Ingresa la altura: "))
    
    # Llama a la función para calcular el área
    area = calcular_area(base, altura)
    
    # Muestra el resultado
    print("El área del triángulo es:", area)

# Llama a la función principal para ejecutar el programa
main()

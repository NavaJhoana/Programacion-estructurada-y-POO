def calcular_area_triangulo(base, altura):
    return (base * altura) / 2

def sumar_numeros(num1, num2):
    return num1 + num2

def main():
    print("=== Cálculo del área de un triángulo ===")
    base = float(input("Ingresa la base: "))
    altura = float(input("Ingresa la altura: "))
    area = calcular_area_triangulo(base, altura)
    print(f"El área del triángulo es: {area}")

    print("\n=== Suma de dos números ===")
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
    suma = sumar_numeros(num1, num2)
    print(f"La suma es: {suma}")

# Ejecutar el programa
main()

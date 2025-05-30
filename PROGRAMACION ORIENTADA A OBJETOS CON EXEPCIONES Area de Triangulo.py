if __name__ == '__main__':
    try:
        print("Ingresa la base")
        b = float(input())
        print("Ingresa la altura")
        h = float(input())
        area = (b * h) / 2
        print("El área del triángulo es:", area)
    except ValueError:
        print("Error: Solo se permiten números")

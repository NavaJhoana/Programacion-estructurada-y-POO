import tkinter as tk

def calcular_area():
    try:
        base = float(entry_base.get())
        altura = float(entry_altura.get())
        area = (base * altura) / 2
        resultado_area.config(text=f"Área: {area}")
    except ValueError:
        resultado_area.config(text="Error: Ingresa números válidos")

def sumar():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        suma = num1 + num2
        resultado_suma.config(text=f"Suma: {suma}")
    except ValueError:
        resultado_suma.config(text="Error: Ingresa números válidos")

def crear_interfaz():
    ventana = tk.Tk()
    ventana.title("Área y Suma con Funciones")
    ventana.geometry("300x300")

    tk.Label(ventana, text="Cálculo del Área del Triángulo").pack()
    tk.Label(ventana, text="Base:").pack()
    global entry_base
    entry_base = tk.Entry(ventana)
    entry_base.pack()

    tk.Label(ventana, text="Altura:").pack()
    global entry_altura
    entry_altura = tk.Entry(ventana)
    entry_altura.pack()

    tk.Button(ventana, text="Calcular Área", command=calcular_area).pack()
    global resultado_area
    resultado_area = tk.Label(ventana, text="")
    resultado_area.pack()

    tk.Label(ventana, text="").pack()
    
    tk.Label(ventana, text="Suma de Dos Números").pack()
    tk.Label(ventana, text="Número 1:").pack()
    global entry_num1
    entry_num1 = tk.Entry(ventana)
    entry_num1.pack()

    tk.Label(ventana, text="Número 2:").pack()
    global entry_num2
    entry_num2 = tk.Entry(ventana)
    entry_num2.pack()

    tk.Button(ventana, text="Sumar", command=sumar).pack()
    global resultado_suma
    resultado_suma = tk.Label(ventana, text="")
    resultado_suma.pack()

    ventana.mainloop()

crear_interfaz()

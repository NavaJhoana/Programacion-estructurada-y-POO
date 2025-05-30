import tkinter as tk
from tkinter import messagebox

def calcular_area():
    try:
        base = float(entrada_base.get())
        altura = float(entrada_altura.get())
        area = (base * altura) / 2
        resultado.config(text=f"El área del triángulo es: {area:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Solo se permiten números")
        resultado.config(text="")  

def main():
    global entrada_base, entrada_altura, resultado

    ventana = tk.Tk()
    ventana.title("Cálculo de Área de Triángulo")
    ventana.geometry("300x250")
    ventana.configure(bg="white")

    tk.Label(ventana, text="Ingresa la base:", bg="white").pack(pady=5)
    entrada_base = tk.Entry(ventana)
    entrada_base.pack(pady=5)

    tk.Label(ventana, text="Ingresa la altura:", bg="white").pack(pady=5)
    entrada_altura = tk.Entry(ventana)
    entrada_altura.pack(pady=5)

    tk.Button(ventana, text="Calcular Área", command=calcular_area, bg="lightgreen", fg="white").pack(pady=10)

    resultado = tk.Label(ventana, text="", bg="white", fg="blue", font=("Arial", 12, "bold"))
    resultado.pack(pady=10)

    ventana.mainloop()

if __name__ == '__main__':
    main()

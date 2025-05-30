import tkinter as tk
from tkinter import messagebox

class AreaTrianguloApp:
    def __init__(self, master):
        self.master = master
        master.title("Área del Triángulo")
        master.geometry("300x250")
        master.configure(bg="white")

        tk.Label(master, text="Ingresa la base:", bg="white").pack(pady=5)
        self.entrada_base = tk.Entry(master)
        self.entrada_base.pack(pady=5)

        tk.Label(master, text="Ingresa la altura:", bg="white").pack(pady=5)
        self.entrada_altura = tk.Entry(master)
        self.entrada_altura.pack(pady=5)

        self.resultado = tk.Label(master, text="", bg="white", fg="blue", font=("Arial", 12, "bold"))
        self.resultado.pack(pady=10)

        self.boton_calcular = tk.Button(master, text="Calcular Área", bg="lightblue", fg="white", command=self.calcular_area)
        self.boton_calcular.pack(pady=10)

    def calcular_area(self):
        try:
            base = float(self.entrada_base.get())
            altura = float(self.entrada_altura.get())
            area = (base * altura) / 2
            self.resultado.config(text=f"El área del triángulo es: {area:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Solo se permiten números")
            self.resultado.config(text="")

if __name__ == '__main__':
    root = tk.Tk()
    app = AreaTrianguloApp(root)
    root.mainloop()

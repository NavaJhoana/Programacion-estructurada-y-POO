import tkinter as tk

class AplicacionSuma:
    def __init__(self, root):
        self.root = root
        self.root.title("Suma")
        self.root.geometry("500x300")
        self.root.config(bg="cornsilk")

        self.crear_interfaz()

    def crear_interfaz(self):
        # Etiqueta y entrada para el primer número
        self.etiqueta1 = tk.Label(self.root, text="Ingresa el número 1:", bg="thistle")
        self.etiqueta1.pack()
        self.entrada1 = tk.Entry(self.root)
        self.entrada1.pack()

        # Etiqueta y entrada para el segundo número
        self.etiqueta2 = tk.Label(self.root, text="Ingresa el número 2:", bg="thistle")
        self.etiqueta2.pack()
        self.entrada2 = tk.Entry(self.root)
        self.entrada2.pack()

        # Botón para realizar la suma
        self.boton = tk.Button(self.root, text="Suma", command=self.sumar)
        self.boton.pack()

        # Etiqueta para mostrar el resultado
        self.resultado = tk.Label(self.root, text="")
        self.resultado.pack()

        # Etiqueta con el autor
        self.etiqueta_autor = tk.Label(self.root, text="Autor: Jhoana Nava Bautista", bg="thistle", font=("Helvetica", 10, "italic"))
        self.etiqueta_autor.pack(side="bottom", pady=5)

    def sumar(self):
        try:
            num1 = float(self.entrada1.get())
            num2 = float(self.entrada2.get())
            suma = num1 + num2
            self.resultado.config(text=f"Resultado de la suma: {suma}")
        except ValueError:
            self.resultado.config(text="Por favor, ingresa números válidos.")

# Crear y ejecutar la aplicación
if __name__ == "__main__":
    ventana = tk.Tk()
    app = AplicacionSuma(ventana)
    ventana.mainloop()

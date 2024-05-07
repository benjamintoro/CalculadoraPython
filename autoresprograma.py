import tkinter as tk

class AutoresPrograma(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Autores del programa")
        self.geometry("600x200")
        self.configure(bg='midnightblue')

        self.mostrar_informacion()

    def mostrar_informacion(self):
        tk.Label(self, text="Autores del programa", font=("Helvetica", 16), bg="midnightblue", fg="white" ).pack(pady=10)

        tk.Label(self, text="Nombres: Benjamin Toro, Matias Soto, Maicol Reyes, Jose Velazquez", font=("Helvetica", 12),bg="midnightblue", fg="white" ).pack(pady=5)
        tk.Label(self, text="Fecha: 19 de Diciembre del 2023", font=("Helvetica", 12), bg="midnightblue", fg="white" ).pack(pady=5)
        tk.Label(self, text="Asignatura: Funciones y Matrices", font=("Helvetica", 12),bg="midnightblue", fg="white" ).pack(pady=5)
        tk.Label(self, text="Profesor: Sebastian Herrera de la Piedra", font=("Helvetica", 12) ,bg="midnightblue", fg="white").pack(pady=5)

if __name__ == "__main__":
    app = AutoresPrograma()
    app.mainloop()

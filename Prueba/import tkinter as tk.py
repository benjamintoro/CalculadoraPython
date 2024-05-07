import tkinter as tk
from tkinter import messagebox

class CalculadoraPromedioApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Calculadora de Promedio")
        self.geometry("1920x1080")

        # Configurar el color de fondo del widget principal (self)
        self.configure(bg='blue')

        # Frame para las notas y pesos
        frame_notas_pesos = tk.Frame(self, bg='blue')  # Configurar el color de fondo del frame
        frame_notas_pesos.pack(side=tk.TOP, pady=10)

        self.label_notas1 = tk.Label(frame_notas_pesos, text="Ingrese la nota 1:", bg='blue', fg='white')  # Configurar colores de texto y fondo
        self.label_notas1.grid(row=0, column=0, padx=10)

        self.entry_notas1 = tk.Entry(frame_notas_pesos, bg='lightgray')  # Configurar color de fondo del Entry
        self.entry_notas1.grid(row=0, column=1, pady=10)

        self.label_pesos1 = tk.Label(frame_notas_pesos, text="Porcentaje nota 1 (%):", bg='blue', fg='white')
        self.label_pesos1.grid(row=0, column=2, padx=10)

        self.entry_pesos1 = tk.Entry(frame_notas_pesos, bg='lightgray')
        self.entry_pesos1.grid(row=0, column=3, pady=10)

        self.label_notas2 = tk.Label(frame_notas_pesos, text="Ingrese la nota 2:", bg='blue', fg='white')
        self.label_notas2.grid(row=1, column=0, padx=10)

        self.entry_notas2 = tk.Entry(frame_notas_pesos, bg='lightgray')
        self.entry_notas2.grid(row=1, column=1, pady=10)

        self.label_pesos2 = tk.Label(frame_notas_pesos, text="Porcentaje nota 2 (%):", bg='blue', fg='white')
        self.label_pesos2.grid(row=1, column=2, padx=10)

        self.entry_pesos2 = tk.Entry(frame_notas_pesos, bg='lightgray')
        self.entry_pesos2.grid(row=1, column=3, pady=10)

        self.label_notas3 = tk.Label(frame_notas_pesos, text="Ingrese la nota 3:", bg='blue', fg='white')
        self.label_notas3.grid(row=2, column=0, padx=10)

        self.entry_notas3 = tk.Entry(frame_notas_pesos, bg='lightgray')
        self.entry_notas3.grid(row=2, column=1, pady=10)

        self.label_pesos3 = tk.Label(frame_notas_pesos, text="Porcentaje nota 3 (%):", bg='blue', fg='white')
        self.label_pesos3.grid(row=2, column=2, padx=10)

        self.entry_pesos3 = tk.Entry(frame_notas_pesos, bg='lightgray')
        self.entry_pesos3.grid(row=2, column=3, pady=10)

        self.label_notas4 = tk.Label(frame_notas_pesos, text="Ingrese la nota 4:", bg='blue', fg='white')
        self.label_notas4.grid(row=3, column=0, padx=10)

        self.entry_notas4 = tk.Entry(frame_notas_pesos, bg='lightgray')
        self.entry_notas4.grid(row=3, column=1, pady=10)

        self.label_pesos4 = tk.Label(frame_notas_pesos, text="Porcentaje nota 4 (%):", bg='blue', fg='white')
        self.label_pesos4.grid(row=3, column=2, padx=10)

        self.entry_pesos4 = tk.Entry(frame_notas_pesos, bg='lightgray')
        self.entry_pesos4.grid(row=3, column=3, pady=10)

        # Menú desplegable para seleccionar el tipo de promedio
        opciones_promedio = ["Seleccionar Promedio", "Promedio Ponderado", "Promedio Simple"]
        self.menu_var = tk.StringVar(self)
        self.menu_var.set(opciones_promedio[0])  # Configuramos el valor inicial

        self.menu_promedio = tk.OptionMenu(self, self.menu_var, *opciones_promedio)
        self.menu_promedio.pack(side=tk.TOP, pady=10)

        # Botón para calcular el promedio
        self.btn_calcular = tk.Button(self, text="Calcular", command=self.calcular_promedio)
        self.btn_calcular.pack(side=tk.TOP, pady=10)

    def calcular_promedio(self):
        tipo_promedio = self.menu_var.get()

        if tipo_promedio == "Seleccionar Promedio":
            messagebox.showerror("Error", "Seleccione un tipo de promedio.")
            return

        try:
            notas = [
                float(self.entry_notas1.get()),
                float(self.entry_notas2.get()),
                float(self.entry_notas3.get()),
                float(self.entry_notas4.get())
            ]

            if tipo_promedio == "Promedio Ponderado":
                pesos = [
                    float(self.entry_pesos1.get()),
                    float(self.entry_pesos2.get()),
                    float(self.entry_pesos3.get()),
                    float(self.entry_pesos4.get())
                ]

                promedio = sum(nota * peso for nota, peso in zip(notas, pesos)) / sum(pesos)

            elif tipo_promedio == "Promedio Simple":
                promedio = sum(notas) / len(notas)

            mensaje_situacion = f"El {tipo_promedio.lower()} es: {promedio:.2f}"

            # Agregar mensaje de la situación del estudiante
            if promedio < 40:
                mensaje_situacion += "\nSituación: Usted lamentablente esta Reprobado"
            elif promedio < 50:
                mensaje_situacion += "\nSituación: Felicitaciones estas Aprobado"
            else:
                mensaje_situacion += "\nSituación:  Excelente trabajo estas Eximido del examen"

            messagebox.showinfo("Resultado", mensaje_situacion)

        except ValueError:
            messagebox.showerror("Error", "Ingrese números válidos.")

if __name__ == "__main__":
    app = CalculadoraPromedioApp()
    app.mainloop()

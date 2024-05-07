import tkinter as tk
from tkinter import messagebox

class CalculadoraPromedioApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Calculadora de Promedio")
        self.geometry("1024x768")

        self.configure(bg='midnight blue')

        # Frame para las notas y porcentajes
        self.frame_notas_porcentajes = tk.Frame(self)
        self.frame_notas_porcentajes.pack(side=tk.TOP, pady=10)

        self.create_widgets_notas(4)  # Crear widgets para las 4 notas iniciales

        # Menú desplegable para seleccionar el tipo de promedio
        opciones_promedio = ["=======SELECCIONA EL PROMEDIO======  ", "Promedio Ponderado", "Promedio Aritmetico"]
        self.menu_var = tk.StringVar(self)
        self.menu_var.set(opciones_promedio[0])  # Configuramos el valor inicial

        self.menu_promedio = tk.OptionMenu(self, self.menu_var, *opciones_promedio)
        self.menu_promedio.pack(side=tk.TOP, pady=10)

        # Botón para agregar notas
        self.btn_agregar_nota = tk.Button(self, text="  AGREGAR NOTA  ", command=self.agregar_nota)
        self.btn_agregar_nota.pack(side=tk.TOP, pady=10)

        # Botón para calcular el promedio
        self.btn_calcular = tk.Button(self, text="    CALCULAR    ", command=self.calcular_promedio)
        self.btn_calcular.pack(side=tk.TOP, pady=20)

    def create_widgets_notas(self, num_notas):
        self.entries_notas = []
        self.entries_porcentajes = []

        for i in range(num_notas):
            label_nota = tk.Label(self.frame_notas_porcentajes, text=f"Ingrese la nota {i + 1}:")
            label_nota.grid(row=i, column=0, padx=10)

            entry_nota = tk.Entry(self.frame_notas_porcentajes)
            entry_nota.grid(row=i, column=1, pady=10)
            self.entries_notas.append(entry_nota)

            label_porcentaje = tk.Label(self.frame_notas_porcentajes, text=f"Porcentaje nota {i + 1} (%):")
            label_porcentaje.grid(row=i, column=2, padx=10)

            entry_porcentaje = tk.Entry(self.frame_notas_porcentajes)
            entry_porcentaje.grid(row=i, column=3, pady=10)
            self.entries_porcentajes.append(entry_porcentaje)

    def agregar_nota(self):
        # Incrementar el contador de notas
        num_notas = len(self.entries_notas) + 1

        # Crear nuevos widgets para la nueva nota
        label_nota = tk.Label(self.frame_notas_porcentajes, text=f"Ingrese la nota {num_notas}:")
        label_nota.grid(row=num_notas - 1, column=0, padx=10)

        entry_nota = tk.Entry(self.frame_notas_porcentajes)
        entry_nota.grid(row=num_notas - 1, column=1, pady=10)
        self.entries_notas.append(entry_nota)

        label_porcentaje = tk.Label(self.frame_notas_porcentajes, text=f"Porcentaje nota {num_notas} (%):")
        label_porcentaje.grid(row=num_notas - 1, column=2, padx=10)

        entry_porcentaje = tk.Entry(self.frame_notas_porcentajes)
        entry_porcentaje.grid(row=num_notas - 1, column=3, pady=10)
        self.entries_porcentajes.append(entry_porcentaje)

    def calcular_promedio(self):
        tipo_promedio = self.menu_var.get()

        if tipo_promedio == "=======SELECCIONA EL PROMEDIO======  ":
            messagebox.showerror("Error", "Seleccione un tipo de promedio.")
            return

        try:
            notas = [float(entry.get()) for entry in self.entries_notas]
            porcentajes = [float(entry.get()) for entry in self.entries_porcentajes]

            if tipo_promedio == "Promedio Ponderado":
                promedio = sum(nota * porcentaje for nota, porcentaje in zip(notas, porcentajes)) / sum(porcentajes)

            elif tipo_promedio == "Promedio Aritmetico":
                promedio = sum(notas) / len(notas)

            # Verificar la situación basada en el promedio calculado
            if promedio < 40:
                situacion = "Reprobado"
            elif 40 <= promedio < 50:
                situacion = "Aprobado"
            else:
                situacion = "Eximido"

            # Mostrar el resultado con la situación del estudiante
            messagebox.showinfo("Resultado", f"El {tipo_promedio.lower()} es: {promedio:.2f}\nSituación: {situacion}")

        except ValueError:
            messagebox.showerror("Error", "Ingrese números válidos.")

if __name__ == "__main__":
    app = CalculadoraPromedioApp()
    app.mainloop()

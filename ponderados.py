import tkinter as tk
from tkinter import messagebox, simpledialog

class CalculadoraPromedioPonderados(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Calculadora de Promedio Ponderado")
        self.geometry("1024x860")
        self.configure(bg="midnightblue")

        # Frame para las notas y porcentajes
        self.frame_notas_porcentajes = tk.Frame(self)
        self.frame_notas_porcentajes.pack(side=tk.TOP, pady=10)

        self.create_widgets_notas(4)  # Variable para crear las 4 notas iniciales

        # Botón para agregar notas
        self.btn_agregar_nota = tk.Button(self, text="   AGREGAR NOTA   ", command=self.agregar_nota)
        self.btn_agregar_nota.pack(side=tk.TOP, pady=10)

        # Botón para quitar notas
        self.btn_quitar_nota = tk.Button(self, text="     QUITAR NOTA     ", command=self.quitar_nota)
        self.btn_quitar_nota.pack(side=tk.TOP, pady=10)

        # Botón para calcular el promedio ponderado
        self.btn_calcular = tk.Button(self, text="       CALCULAR       ", command=self.calcular_promedio_ponderado)
        self.btn_calcular.pack(side=tk.TOP, pady=10)

    def create_widgets_notas(self, num_notas):
        self.entries_notas = []
        self.entries_porcentajes = []
        self.labels_notas = []
        self.labels_porcentajes = []

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

            self.labels_notas.append(label_nota)
            self.labels_porcentajes.append(label_porcentaje)

    # Funcion para agregar notas
    def agregar_nota(self):
        # Incrementar el contador de notas
        num_notas = len(self.entries_notas) + 1

        # Restringir a un máximo de 10 notas
        if num_notas > 10:
            messagebox.showwarning("Advertencia", "Se ha alcanzado el límite máximo de 10 notas.")
            return

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

        self.labels_notas.append(label_nota)
        self.labels_porcentajes.append(label_porcentaje)

    # Funcion para quitar notas
    def quitar_nota(self):
        try:
            if len(self.labels_notas) > 1:
                self.entries_notas[-1].destroy()
                self.entries_porcentajes[-1].destroy()

                self.labels_notas[-1].destroy()
                self.labels_porcentajes[-1].destroy()

                del self.entries_notas[-1]
                del self.entries_porcentajes[-1]
                del self.labels_notas[-1]
                del self.labels_porcentajes[-1]

            else:
                messagebox.showwarning("Advertencia", "Debe dejar al menos una nota.")

        except Exception as e:
            print(f"Error al quitar nota: {e}")

    # Funcion para Calcular el promedio
    def calcular_promedio_ponderado(self):
        try:
            notas = [float(entry.get()) for entry in self.entries_notas]
            porcentajes = [float(entry.get()) for entry in self.entries_porcentajes]

            promedio = sum(nota * porcentaje for nota, porcentaje in zip(notas, porcentajes)) / sum(porcentajes)

            # Verificar la situación basada en el promedio calculado
            if promedio < 40:
                situacion = "Usted está Reprobado"
            elif 40 <= promedio < 49:
                situacion = "Usted está Aprobado"
            else:
                situacion = "Usted está Eximido"

            # Mostrar el resultado con la situación del estudiante
            mensaje = f"El promedio ponderado es: {promedio:.2f}\nSituación: {situacion}"

            # Mostrar el mensaje antes de preguntar por el examen
            messagebox.showinfo("Resultado", mensaje)

            # Preguntar si desea agregar un examen
            respuesta_examen = messagebox.askyesno("Agregar Examen", "¿Desea agregar un examen?")

            if respuesta_examen:
                nota_examen = simpledialog.askfloat("Nota del Examen", "Ingrese la nota del examen (10-70):",
                                                    minvalue=10, maxvalue=70)
                porcentaje_examen = simpledialog.askfloat("Porcentaje del Examen", "Ingrese el porcentaje del examen (%):",
                                                        minvalue=0, maxvalue=100)

                # Ajustar el promedio con la nueva nota del examen y su porcentaje
                porcentaje_examen /= 100  # Convertir el porcentaje a decimal
                promedio_final = (1 - porcentaje_examen) * promedio + porcentaje_examen * nota_examen

                mensaje_examen = f"\nNota del examen: {nota_examen}\nPorcentaje del examen: {porcentaje_examen * 100}%"
                mensaje_examen += f"\nPromedio final con examen: {promedio_final:.2f}"

                # Mostrar el mensaje final con la situación y el examen
                messagebox.showinfo("Resultado Final", mensaje + mensaje_examen)

        except ValueError:
            messagebox.showerror("Error", "Ingrese números válidos.")

if __name__ == "__main__":
    app = CalculadoraPromedioPonderados()
    app.mainloop()

import tkinter as tk
from tkinter import messagebox, simpledialog

class CalculadoraPromedioAritmeticos:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora Aritmetica")
        self.root.configure(bg='midnightblue')
        self.root.geometry("1024x860")

        # Frame para las notas
        self.frame_notas = tk.Frame(root)
        self.frame_notas.pack(side=tk.TOP, pady=10)

        self.etiquetas = []
        self.entradas = []

        for i in range(4):
            etiqueta = tk.Label(self.frame_notas, text=f"Nota {i + 1}:")
            etiqueta.grid(row=i, column=0, padx=10, pady=10)
            self.etiquetas.append(etiqueta)

            entrada = tk.Entry(self.frame_notas)
            entrada.grid(row=i, column=1, padx=10, pady=10)
            self.entradas.append(entrada)

        # Botón para agregar notas
        self.boton_anadir_nota = tk.Button(root, text="            AÑADIR NOTA           ", command=self.anadir_nota)
        self.boton_anadir_nota.pack(side=tk.TOP, pady=10)

        # Botón para quitar notas
        self.boton_quitar_nota = tk.Button(root, text="            QUITAR NOTA           ", command=self.quitar_nota)
        self.boton_quitar_nota.pack(side=tk.TOP, pady=10)

        # Botón para calcular el promedio ponderado
        self.boton_calcular = tk.Button(root, text="    CALCULAR PROMEDIO    ", command=self.mostrar_promedio)
        self.boton_calcular.pack(side=tk.TOP, pady=10)

    # Funcion para Calcular el promedio
    def calcular_promedio(self):
        try:
            notas = [float(entrada.get()) for entrada in self.entradas]
            promedio = sum(notas) / len(notas)
            return promedio

        except ValueError:
            messagebox.showerror("Error", "Ingrese números válidos.")

    # Funcion que muestra el promedio y da la opción de agregar un examen
    def mostrar_promedio(self):
        promedio = self.calcular_promedio()

        if promedio is not None:
            mensaje = f"Su promedio es de: {promedio:.2f}\n"

            if promedio >= 40:
                mensaje += "Usted ha aprobado la asignatura."
            else:
                mensaje += "Usted ha reprobado la asignatura."

            # Mostrar el mensaje del promedio y la situación
            messagebox.showinfo("Resultado del Promedio", mensaje)

            # Preguntar si desea agregar un examen
            respuesta_examen = messagebox.askyesno("Agregar Examen", "¿Desea agregar un examen?")

            if respuesta_examen:
                self.calcular_examen()

    # Funcion que hace el calculo del examen
    def calcular_examen(self):
        try:
            nota_examen = simpledialog.askfloat("Nota del Examen", "Ingrese la nota del examen:", minvalue=10, maxvalue=70)
            promedio = self.calcular_promedio()
            promedio_final = 0.75 * promedio + 0.25 * nota_examen

            mensaje = f"Su promedio final es de: {promedio_final:.2f}\n"

            if promedio_final >= 40:
                mensaje += "Usted ha aprobado la asignatura."
            else:
                mensaje += "Usted ha reprobado la asignatura."

            messagebox.showinfo("Resultado del Examen", mensaje)

        except ValueError:
            messagebox.showerror("Error", "Ingrese una nota válida para el examen.")

    # Funcion para agregar notas
    def anadir_nota(self):
        try:
            if len(self.etiquetas) < 10:
                nueva_nota = tk.Entry(self.frame_notas)
                nueva_nota.grid(row=len(self.etiquetas), column=1, padx=10, pady=10, sticky='nsew')
                self.entradas.append(nueva_nota)

                nueva_etiqueta = tk.Label(self.frame_notas, text=f"Nota {len(self.etiquetas) + 1}:")
                nueva_etiqueta.grid(row=len(self.etiquetas), column=0, padx=10, pady=10, sticky='nsew')
                self.etiquetas.append(nueva_etiqueta)
            else:
                messagebox.showwarning("Advertencia", "Se ha excedido el límite máximo de 10 notas.")

        except Exception as e:
            print(f"Error al añadir nota: {e}")

    # Funcion para quitar notas
    def quitar_nota(self):
        try:
            if len(self.etiquetas) > 1:
                self.entradas[-1].destroy()
                self.etiquetas[-1].destroy()

                del self.entradas[-1]
                del self.etiquetas[-1]
            else:
                messagebox.showwarning("Advertencia", "Debe dejar al menos una nota.")
        except Exception as e:
            print(f"Error al quitar nota: {e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraPromedioAritmeticos(root)
    root.mainloop()

import tkinter as tk
from tkinter import messagebox

class CalculadoraPromedioApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Calculadora de Promedios")
        self.geometry("1024x860")
        #self.iconbitmap('D:\\Jogos\\Calculadora\\calculadora.ico')

        # Configurar el color de fondo del widget principal (self)
        self.configure(bg='midnight blue')

        # Crear un Canvas para el fondo
        #self.canvas = tk.Canvas(self, width=1920, height=1080, bg='blue')
        #self.canvas.pack(expand=tk.YES, fill=tk.BOTH)

        # Cargar la imagen de fondo
        #self.imagen_fondo = tk.PhotoImage(file='D:\\Jogos\\Calculadora\\fondomat.png')
        # self.canvas.create_image(0, 0, anchor=tk.NW, image=self.imagen_fondo)


        # Frame para las notas y porcentajes
        frame_notas_porcentajes = tk.Frame(self)  
        frame_notas_porcentajes.pack(side=tk.TOP, pady=10)

        self.label_notas1 = tk.Label(frame_notas_porcentajes, text="Ingrese la Nota 1:")
        self.label_notas1.grid(row=0, column=0, padx=10)

        self.entry_notas1 = tk.Entry(frame_notas_porcentajes,)
        self.entry_notas1.grid(row=0, column=1, pady=10)

        self.label_porcentajes1 = tk.Label(frame_notas_porcentajes, text="Porcentaje Nota 1 (%):")
        self.label_porcentajes1.grid(row=0, column=2, padx=10)

        self.entry_porcentajes1 = tk.Entry(frame_notas_porcentajes,)
        self.entry_porcentajes1.grid(row=0, column=3, pady=10)

        self.label_notas2 = tk.Label(frame_notas_porcentajes, text="Ingrese la Nota 2:")
        self.label_notas2.grid(row=1, column=0, padx=10)

        self.entry_notas2 = tk.Entry(frame_notas_porcentajes,)
        self.entry_notas2.grid(row=1, column=1, pady=10)

        self.label_porcentajes2 = tk.Label(frame_notas_porcentajes, text="Porcentaje Nota 2 (%):")
        self.label_porcentajes2.grid(row=1, column=2, padx=10)

        self.entry_porcentajes2 = tk.Entry(frame_notas_porcentajes,)
        self.entry_porcentajes2.grid(row=1, column=3, pady=10)

        self.label_notas3 = tk.Label(frame_notas_porcentajes, text="Ingrese la Nota 3:")
        self.label_notas3.grid(row=2, column=0, padx=10)

        self.entry_notas3 = tk.Entry(frame_notas_porcentajes,)
        self.entry_notas3.grid(row=2, column=1, pady=10)

        self.label_porcentajes3 = tk.Label(frame_notas_porcentajes, text="Porcentaje Nota 3 (%):")
        self.label_porcentajes3.grid(row=2, column=2, padx=10)

        self.entry_porcentajes3 = tk.Entry(frame_notas_porcentajes,)
        self.entry_porcentajes3.grid(row=2, column=3, pady=10)

        self.label_notas4 = tk.Label(frame_notas_porcentajes, text="Ingrese la Nota 4:")
        self.label_notas4.grid(row=3, column=0, padx=10)

        self.entry_notas4 = tk.Entry(frame_notas_porcentajes,)
        self.entry_notas4.grid(row=3, column=1, pady=10)

        self.label_porcentajes4 = tk.Label(frame_notas_porcentajes, text="Porcentaje Nota 4 (%):")
        self.label_porcentajes4.grid(row=3, column=2, padx=10)

        self.entry_porcentajes4 = tk.Entry(frame_notas_porcentajes,)
        self.entry_porcentajes4.grid(row=3, column=3, pady=10)

        # Nueva sección para el examen
        self.label_examen = tk.Label(frame_notas_porcentajes, text="Ingrese la Nota del examen:")
        self.label_examen.grid(row=4, column=0, padx=10)

        self.entry_examen = tk.Entry(frame_notas_porcentajes,)
        self.entry_examen.grid(row=4, column=1, pady=10)

        # porcentaje del examen
        self.label_porcentaje_examen = tk.Label(frame_notas_porcentajes, text="Porcentaje del examen (%):")
        self.label_porcentaje_examen.grid(row=4, column=2, padx=10)

        self.entry_porcentaje_examen = tk.Entry(frame_notas_porcentajes,)
        self.entry_porcentaje_examen.grid(row=4, column=3, pady=10)

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
                porcentajes = [
                    float(self.entry_porcentajes1.get()),
                    float(self.entry_porcentajes2.get()),
                    float(self.entry_porcentajes3.get()),
                    float(self.entry_porcentajes4.get())
                ]

                promedio = sum(nota * porcentaje for nota, porcentaje in zip(notas, porcentajes)) / sum(porcentajes)

                # Agregar la nota del examen ponderada
                examen = float(self.entry_examen.get()) if self.entry_examen.get() else 0
                porcentaje_examen = float(self.entry_porcentaje_examen.get()) if self.entry_porcentaje_examen.get() else 0

                promedio_final = promedio + (examen * porcentaje_examen / 100)

            elif tipo_promedio == "Promedio Simple":
                promedio = sum(notas) / len(notas)
                promedio_final = promedio

            # Determinar la situación
            situacion = ""
            if promedio_final < 40:
                situacion = f"\nSituación: Reprobado"
            elif promedio_final < 50:
                situacion = f"\nSituación: Aprobado"
            else:
                situacion = f"\nSituación: Eximido"

            mensaje_situacion = f"El {tipo_promedio.lower()} es: {promedio_final:.2f}" + situacion
            messagebox.showinfo("Resultado", mensaje_situacion)

        except ValueError:
            messagebox.showerror("Error", "Ingrese números válidos.")

if __name__ == "__main__":
    app = CalculadoraPromedioApp()
    app.mainloop()

import tkinter as tk
from ponderados import CalculadoraPromedioPonderados  
from aritmeticos import CalculadoraPromedioAritmeticos
from autoresprograma import AutoresPrograma

class MainMenu(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Menú Principal")
        self.geometry("400x400")


        self.configure(bg='midnightblue')

        # Creamos el menu con herencia entre archivos

        tk.Label(self, text="CALCULADORA DE PROMEDIOS", font=("Arial", 18, "bold"),bg='midnightblue', fg="White").pack(pady=10)

        tk.Label(self, text="¿Que promedio desea calcular?", font=("Arial", 18, "bold"), bg='midnightblue', fg="White").pack(pady=10)
   
        self.btn_ponderado = tk.Button(self, text="Promedio Ponderado", command=self.abrir_calculadora_ponderada)
        self.btn_ponderado.pack(pady=20)

        self.btn_aritmmetico = tk.Button(self, text="Promedio Aritmetico", command=self.abrir_calculadora_aritmetica)
        self.btn_aritmmetico.pack(pady=20)

        self.btn_autorprograma = tk.Button(self, text="Autores del Programa", command=self.autores_programa)
        self.btn_autorprograma.pack(pady=20)

        self.btn_salir = tk.Button(self, text="Salir", command=self.destroy)
        self.btn_salir.pack()


    # Funciones para abrir programas herenciados
    
    def abrir_calculadora_ponderada(self):
        app = CalculadoraPromedioPonderados()
        app.mainloop()

    def abrir_calculadora_aritmetica(self):

        root = tk.Tk()
        app = CalculadoraPromedioAritmeticos(root)
        root.mainloop()

    def autores_programa(self):
        app = AutoresPrograma()





if __name__ == "__main__":
    main_menu = MainMenu()
    main_menu.mainloop()

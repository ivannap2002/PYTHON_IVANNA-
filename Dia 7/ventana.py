import os
import platform
from tkinter import *
from tkinter import messagebox

# Crear la ventana principal
ventana = Tk()
ventana.title("Primera Ventana")
ventana.geometry("520x480")

# Función para abrir la calculadora
def abrir_calculadora():
    if platform.system() == "Windows":
        os.system("start calc.exe")
    else:
        messagebox.showerror("Error", "Este script solo está configurado para Windows.")

# Crear el botón
boton = Button(ventana, text="Abrir calculadora", command=abrir_calculadora)
boton.place(x=50, y=50)

# Iniciar el loop principal de la ventana
ventana.mainloop()

from tkinter import Tk, Label, Button, Entry, font
import tkinter as tk
from tkinter import ttk


# Genero mi ventana
windows = Tk()
windows.title("Mi proyecto final")

# Tamaño de la ventana y diseño
windows.geometry("450x550")
windows.resizable(0,0)


helvfont = font.Font(family="Helvetica", size=14, weight="bold")
lbl1 = Label(windows, text="Restaurant", font=helvfont)#Titulo de la ventana y Diseño de texto
lbl1.place(x=150, y= 10,  width=110, height=50)#posicion

helvfont2 = font.Font(family="Helvetica", size=8, weight="bold")
lbl2 = Label(windows, text="""
    Nuestro restaurante es un lugar donde ofrecemos una 
variedad de platos deliciosos y recursos culinarios
para el publico para satisfacer tus necesidades culinarias
y hacerte disfrutar de una experiencia gastronomica
             """, bg="white", font=helvfont2)#Texto que se muestra para pedir al usuario que digite algo
lbl2.place(x=40, y=120, width=320, height=100)#Diseño de posicion

helvfont3 = font.Font(family="Helvetica", size=10, weight="bold")
btn1 = Button(windows, text="Registrarse", bg="gray", fg="white", font=helvfont3)#Boton para registrarse
btn1.place(x=140, y=250, width=130, height=35)#Diseño de boton y posicion

btn2 = Button(windows, text="Iniciar sesion", bg="gray", fg="white", font=helvfont3)#Boton para iniciar sesion
btn2.place(x=140, y=300, width=130, height=35)#Diseño de boton y posicion


if __name__ == "__main__":
    windows.mainloop()

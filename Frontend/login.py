from tkinter import Tk, Label, Button, Entry, font
import tkinter as tk
from tkinter import ttk

# Genero mi ventana
windows = Tk()
windows.title("Mi proyecto final")

# Tamaño de la ventana
windows.geometry("400x400")
windows.resizable(0,0)

# # Se genera el contenedor de pestañas

tab = ttk.Notebook(windows)

# # Creo mi pestaña 1
# tab_1 = ttk.Frame(tab)
# tab.add(tab_1, text="Inicio")
# # Añadir contenido a la pestaña
# tag1 = tk.Label(tab_1, text="Mi restaurante").pack()


# Creo mi pestaña 2
# tab_2 = ttk.Frame(tab)
# tab.add(tab_2, text="Registro")

# Creo mi pestaña 3
tab_3 = ttk.Frame(tab)
tab.add(tab_3, text="Inicio de sesion")


# Añadir contenido a la pestaña
helvfont = font.Font(family="Helvetica", size=14, weight="bold")
lbl1 = Label(windows, text="Restaurant", font=helvfont)#Titulo de la ventana y Diseño de texto
lbl1.place(x=150, y= 30,  width=110, height=50)#posicion

# Añadir el inicio de sesion
registro = Label(windows,  background="gray")
registro.place(x=100, y= 100,  width=210, height=220)#posicion

helvfont2 = font.Font(family="Helvetica", size=11, weight="bold")
lbl2 = Label(windows, text="Inicio de sesion", font=helvfont2, fg="white", background="gray")#Titulo de la ventana y Diseño de texto
lbl2.place(x=150, y= 100,  width=110, height=40)#posicion

helvfont3 = font.Font(family="Helvetica", size=9, weight="bold")
lbl3 = Label(windows, text="Email", font=helvfont3, fg="white", background="gray")#Titulo de la ventana y Diseño de texto
lbl3.place(x=135, y= 150)#posicion

entryet1 = Entry(windows)#Casilla donde el usuario digita el contenido
entryet1.place(x=130, y=175, width=150, height=20)#Diseño de posicion

lbl4 = Label(windows, text="Contraseña", font=helvfont3, fg="white", background="gray")#Titulo de la ventana y Diseño de texto
lbl4.place(x=135, y= 205)#posicion

entryet1 = Entry(windows)#Casilla donde el usuario digita el contenido
entryet1.place(x=130, y=230, width=150, height=20)#Diseño de posicion


btn1 = Button(windows, text="Iniciar sesion", command="", bg="black", fg="white", font=helvfont3)#Boton para guardar el contenido que el usuario digita
btn1.place(x=160, y=275, width=90, height=30)#Diseño de boton y posicion


# Añadir las pestañas a la ventana
tab.pack(expand=True, fill="both")
# Se ejecuta el bloque de la ventana

windows.mainloop()

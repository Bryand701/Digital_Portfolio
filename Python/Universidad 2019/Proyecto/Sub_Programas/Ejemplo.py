from tkinter import *
import tkinter
import math
def fibonacci(numero):
    if numero == 0:
        return 0
    elif numero == 1:
        return 1
    else:
        return fibonacci(numero-1)+fibonacci(numero-2)

def factorial(numero):
    if numero == 0:
        return 1
    else:
        return numero * factorial(numero-1)

def raizCuadrada(numero):
    return math.sqrt(numero)

# Globales
nombre = ""
principal = tkinter.Tk() #Crea una ventana llamada principal
principal.title("Ingresar")
principal.geometry("500x150")

#Label
labelNombre = Label(principal, text= "Nombre: ", fg ='#4285f4', font = ("Serif", 14))
labelNombre.place(x=15, y= 27)

#TextBox
textBoxNombre = Entry(principal, width=30)
textBoxNombre.place(x=100, y= 30)

def ingresar():
    nombre = textBoxNombre.get()
    # Ocultar la ventana principal
    principal.withdraw()
    # Mostrar la ventana calculadora
    calculadora.update()
    calculadora.deiconify()

#Button
buttonIngresar= Button(principal, text="Ingresar", activebackground="#4285f4", fg = "white", bg = "#db4437", font = ("Serif", 13), width=20, heigh=3, command=ingresar)
buttonIngresar.place(x=300, y=10)

#Menubar
def nada():
  x = 0

menubar = Menu(principal)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Ingresar", command=ingresar)
filemenu.add_separator()
filemenu.add_command(label="Otro", command=nada)
menubar.add_cascade(label="Opciones", menu=filemenu)

principal.config(menu = menubar)


#Ventana Calculadora
calculadora = tkinter.Toplevel()
calculadora.withdraw()
calculadora.title("Cálculos")
calculadora.geometry("650x300")

#Label
labelFibonacci= Label(calculadora, text= "Fibonacci: ", fg =  "#4285f4", font = ("Serif", 14))
labelFibonacci.place(x=100, y= 50)

labelFactorial= Label(calculadora, text= "Factorial: ", fg =  "#4285f4", font = ("Serif", 14))
labelFactorial.place(x=100, y= 100)

labelRaizCuadrada= Label(calculadora, text= "Raiz Cuadrada: ", fg =  "#4285f4", font = ("Serif", 14))
labelRaizCuadrada.place(x=100, y= 150)

#TextBox
textBoxFibonacci = Entry(calculadora, width=7, font = ("Serif", 13))
textBoxFibonacci.place(x=250, y= 50)

textBoxFactorial = Entry(calculadora, width=7, font = ("Serif", 13))
textBoxFactorial.place(x=250, y= 100)

textBoxRaizCuadrada= Entry(calculadora, width=7, font = ("Serif", 13))
textBoxRaizCuadrada.place(x=250, y= 150)

textBoxFibonacciResult = Entry(calculadora, width=12, font = ("Serif", 13))
textBoxFibonacciResult.place(x=450, y= 50)

textBoxFactorialResult = Entry(calculadora, width=12, font = ("Serif", 13))
textBoxFactorialResult.place(x=450, y= 100)

textBoxRaizCuadradaResult = Entry(calculadora, width=12, font = ("Serif", 13))
textBoxRaizCuadradaResult.place(x=450, y= 150)

# CheckButton
varBinario = IntVar()
checkButtonBinario = Checkbutton(calculadora, text = "Desplegar Fibonacci en Binario", variable = varBinario, onvalue = 1, offvalue = 0, height=5, width = 60, )
checkButtonBinario.place(x = 350, y = 200)

def salir():
    # Mostrar la ventana principal
    principal.update()
    principal.deiconify()
    # Ocultar la ventana en la que estoy
    calculadora.withdraw()



def displayFibonacci():
    entry = textBoxFibonacci.get()
    number = int (entry)
    resultado = fibonacci(number)
    print(varBinario.get())
    if varBinario.get() == 1:
        resultado = bin(resultado)
    textBoxFibonacciResult.delete(0, END)
    textBoxFibonacciResult.insert(0,resultado)

def displayFactorial():
    entry = textBoxFactorial.get()
    number = int (entry)
    resultado = factorial(number)
    textBoxFactorialResult.delete(0, END)
    textBoxFactorialResult.insert(0,resultado)

def displayRaizCuadrada():
    entry = textBoxRaizCuadrada.get()
    number = float (entry)
    resultado = raizCuadrada(number)
    textBoxRaizCuadradaResult.delete(0, END)
    textBoxRaizCuadradaResult.insert(0,resultado)

#Button
buttonFibonacci= Button(calculadora, text="Calcular",width=7, activebackground="#4285f4",command= displayFibonacci, fg = "white", bg = "#db4437", font = ("Serif", 13))
buttonFibonacci.place(x=350, y=50)

buttonFactorial= Button(calculadora, text="Calcular",width=7, activebackground="#4285f4",command= displayFactorial, fg = "white", bg = "#db4437", font = ("Serif", 13))
buttonFactorial.place(x=350, y=100)

buttonRaizCuadrado= Button(calculadora, text="Calcular",width=7, activebackground="#4285f4",command= displayRaizCuadrada, fg = "white", bg = "#db4437", font = ("Serif", 13))
buttonRaizCuadrado.place(x=350, y=150)

buttonRaizCuadrado= Button(calculadora, text="Salir",width=7, activebackground="#4285f4",command= salir, fg = "white", bg = "#db4437", font = ("Serif", 13))
buttonRaizCuadrado.place(x=300, y=250)

# Para iniciar el programa
principal.mainloop()

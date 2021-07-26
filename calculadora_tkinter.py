#!/usr/bin/python3
#
# Creando mi primer programa en Tkinter.
# Programa: Calculadora Basica en Tkinter.
# By Blackster.

#importamos los modulos necesarios para nuestro programa.
from tkinter import *

#creacion de nuestra ventana inicial.
root = Tk()
root.title("Calculadora en python3")

#creamos nuestro frame.
frame = Frame(root, height="0", width="300")
frame.pack()


#Clase para nuestra suma.
class sumando:
	def __init__(self):
		v_suma = Tk()
		#variables
		num1 = IntVar()
		num2 =IntVar()
		#creamos nuestros labels y cajas de texto.
		fr = Frame(v_suma, height="0", width="300").pack()
		self.tit = v_suma.title("Sumando con Tkinter")
		self.n1_l = Label(fr, text="Introduce un numero: ").pack()
		self.n1_box = Entry(fr, textvariable=num1).pack()
		self.n2_l = Label(fr, text="Introduce otro numero: ").pack()
		self.n2_box = Entry(fr, textvariable=num2).pack()
		ans = Label(v_suma)
		ans.pack()
		etiqueta = Label(v_suma)
		etiqueta.pack()
		""" funcion que arroja los resultados al oprimir el boton de suma"""
		def sumita():
			f_num = num1.get()
			s_num = num2.get()
			ans.config(text="Resultado de la suma: ")
			etiqueta.config(text=num1.get()+num2.get())
		#creamos nuestro boton de suma.
		self.b_1 = Button(v_suma, text="Sumar", command=sumita).pack()
		v_suma.mainloop()



#Clase para nuestra resta.
class restando:
	def __init__(self):
		v_resta = Tk()
		#variables
		num1 = IntVar()
		num2 =IntVar()
		fr = Frame(v_resta, height="0", width="300").pack()
		self.title = v_resta.title("Restando con Tkinter")
		self.num1_l = Label(v_resta, text="Introduce un numero: ").pack()
		self.num1_box = Entry(fr, textvariable=num1).pack()
		self.num2_l = Label(v_resta, text="Introduce otro numero: ").pack()
		self.num2_box = Entry(fr, textvariable=num2).pack()
		ans = Label(v_resta)
		ans.pack()
		etiqueta = Label(v_resta)
		etiqueta.pack()
		""" funcion que arroja los resultados al oprimir el boton de restar """
		def restica():
			f_num = num1.get()
			s_num = num2.get()
			ans.config(text="Resultado de la resta: ")
			etiqueta.config(text=num1.get()-num2.get())
		self.b1_1 = Button(v_resta, text="Restar", command=restica).pack()
		v_resta.mainloop()


#Clase para nuestra multiplicacion.
class multiplicando:
	def __init__(self):
		v_multi = Tk()
		#variables
		num1 = IntVar()
		num2 =IntVar()
		fr = Frame(v_multi, height="0", width="300").pack()
		self.title = v_multi.title("Multiplicando con Tkinter")
		self.num1_la = Label(v_multi, text="Introduce un numero: ").pack()
		self.num1_box = Entry(fr, textvariable=num1).pack()
		self.num2_la = Label(v_multi, text="Introduce otro numero: ").pack()
		self.num2_box = Entry(fr, textvariable=num2).pack()
		ans = Label(v_multi)
		ans.pack()
		etiqueta = Label(v_multi)
		etiqueta.pack()
		""" funcion que arroja los resultados al oprimir el boton de multiplicar """
		def multiple():
			f_num = num1.get()
			s_num = num2.get()
			ans.config(text="Resultado de la multiplicacion: ")
			etiqueta.config(text=num1.get()*num2.get())
		self.button = Button(v_multi, text="Multiplicar", command=multiple).pack()
		v_multi.mainloop()


#clase para nuestra division.
class dividir:
	def __init__(self):
		v_divi = Tk()
		#variables
		num1 = IntVar()
		num2 =IntVar()
		fr = Frame(v_divi, height="0", width="300").pack()
		self.title = v_divi.title("Dividiendo con Tkinter")
		self.n1_label = Label(v_divi, text="Introduce un numero: ").pack()
		self.num1_box = Entry(fr, textvariable=num1).pack()
		self.n2_label = Label(v_divi, text="Introduce otro numero: ").pack()
		self.num2_box = Entry(fr, textvariable=num2).pack()
		ans = Label(v_divi)
		ans.pack()
		etiqueta = Label(v_divi)
		etiqueta.pack()
		""" funcion que arroja los resultados al oprimir el boton de dividir """
		def divisioncita():
			f_num = num1.get()
			s_num = num2.get()
			ans.config(text="Resultado de la division: ")
			etiqueta.config(text=num1.get()/num2.get())
		self.button = Button(v_divi, text="Dividir", command=divisioncita).pack()
		v_divi.mainloop()



""" funcion que llama a nuestra ventana de suma"""
def sumar():
	root.destroy()
	adicion = sumando()

""" funcion que llama a nuestra ventana de resta"""
def restar():
	root.destroy()
	sustraer = restando()

""" funcion que llama a nuestra ventana de multiplicacion"""
def multiplica():
	root.destroy()
	multi = multiplicando()

""" funcion que llama a nuestra ventana de division"""
def divide():
	root.destroy()
	divide = dividir()


#creando nuestros botones principales.
""" boton que llama a nuestra funcion de suma """
b1 = Button(root, text="Sumar", command=sumar)
b1.pack()
b1.config(justify="center")

""" boton que llama a nuestra funcion de resta """
b2 = Button(root, text="Restar", command=restar)
b2.pack()
b2.config(justify="center")

""" boton que llama a nuestra funcion de multiplicacion """
b3 = Button(root, text="Multiplicar", command=multiplica)
b3.pack()
b3.config(justify="center")

""" boton que llama a nuestra funcion de division """
b4 = Button(root, text="Dividir", command=divide)
b4.pack()
b4.config(justify="center")


root.mainloop()

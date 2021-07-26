#!/usr/bin/env python3
# Simple generador de contraseñas.
# by Blackster

#importamos los modulos necesarios.
from tkinter import *
import random
import time

#creamos nuestra ventana raiz.
root = Tk()
root.title("Password Generator by Blackster")
#creamos nuestro frame.
fr = Frame(root, width="300", height="0").pack()

#creamos las clases de nuestro programa.

""" clase creada para generar contraseñas de 12 caracteres """
class Char12:
    def __init__(self):
        self.vchar12 = Tk()
        self.title = self.vchar12.title("** Generar Password 12 caracteres **")
        self.fr = Frame(self.vchar12, height="0", width="330").pack()
        r1, r2, r3, r4, r5, r6, r7 , r8, r9, r10, r11, r12 = StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar()
        self.letters = ["-", "_", "a", "!", "$", "C", "D", "*", "#", "b", "%", "&", "c", "Z", "/", "(", "d", "A", ")", "=", "B", "e", "?", "¿", "f", "X", "^", "{", "}", "Y", "g", "I", "J", ":", ";", "h", "G", "H", "<", ">", "i", "j", "3", "K", "+", "-", "L", "5", "k", "l", "4", "1", "m", "@", "7", "0" "O", "P", "2", "n", "9", "|", "M", "8", "N", "o", "7", "p", "q", "r", "s", "6", "Q", "R", "5", "t", "u", "1" "S", "4", "T", "v", "w", "6", "V", "3", "W", "E", "2", "F", "x", "y", "z", "1", "[", "]"]
        self.label1 = Label(self.vchar12)
        self.label1.pack()
        self.label = Label(self.vchar12)
        self.label.pack()
        self.text = Text(self.vchar12, height=1)
        self.text.pack()
        """ funcion que arroja nuestra contraseña generada """
        def passgen():
            gen1 = random.randint(0, 93)
            gen2 = random.randint(0, 93)
            gen3 = random.randint(0, 93)
            gen4 = random.randint(0, 93)
            gen5 = random.randint(0, 93)
            gen6 = random.randint(0, 93)
            gen7 = random.randint(0, 93)
            gen8 = random.randint(0, 93)
            gen9 = random.randint(0, 93)
            gen10 = random.randint(0, 93)
            gen11 = random.randint(0, 93)
            gen12 = random.randint(0, 93)

            r1 = self.letters[gen1]
            r2 = self.letters[gen2]
            r3 = self.letters[gen3]
            r4 = self.letters[gen4]
            r5 = self.letters[gen5]
            r6 = self.letters[gen6]
            r7 = self.letters[gen7]
            r8 = self.letters[gen8]
            r9 = self.letters[gen9]
            r10 = self.letters[gen10]
            r11 = self.letters[gen11]
            r12 = self.letters[gen12]
            self.text.insert(1.0, self.letters[gen1]+self.letters[gen2]+self.letters[gen3]+self.letters[gen4]+self.letters[gen5]+self.letters[gen6]+self.letters[gen7]+self.letters[gen8]+self.letters[gen9]+self.letters[gen10]+self.letters[gen11]+self.letters[gen12])
            self.text.config(state="disabled")
            self.label1.config(text="Contraseña generada: ")
            self.label.config(text=self.letters[gen1]+self.letters[gen2]+self.letters[gen3]+self.letters[gen4]+self.letters[gen5]+self.letters[gen6]+self.letters[gen7]+self.letters[gen8]+self.letters[gen9]+self.letters[gen10]+self.letters[gen11]+self.letters[gen12])
        self.boton = Button(self.vchar12, text="Generar Password", command=passgen).pack()
        self.vchar12.mainloop()


""" creamos nuestra segunda clase para generar contraseñas de 16 caracteres """
class Char16:
    def __init__(self):
        self.vchar16 = Tk()
        self.title = self.vchar16.title("*** Generar Password 16 caracteres ***")
        self.fr = Frame(self.vchar16, height=0, width=330).pack()
        r1, r2, r3, r4, r5, r6, r7 , r8, r9, r10, r11, r12 = StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar()
        self.letters = ["-", "_", "a", "!", "$", "C", "D", "*", "#", "b", "%", "&", "c", "Z", "/", "(", "d", "A", ")", "=", "B", "e", "?", "¿", "f", "X", "^", "{", "}", "Y", "g", "I", "J", ":", ";", "h", "G", "H", "<", ">", "i", "j", "3", "K", "+", "-", "L", "5", "k", "l", "4", "1", "m", "@", "7", "0" "O", "P", "2", "n", "9", "|", "M", "8", "N", "o", "7", "p", "q", "r", "s", "6", "Q", "R", "5", "t", "u", "1" "S", "4", "T", "v", "w", "6", "V", "3", "W", "E", "2", "F", "x", "y", "z", "1", "[", "]"]
        self.label1 = Label(self.vchar16)
        self.label1.pack()
        self.label = Label(self.vchar16)
        self.label.pack()
        self.text = Text(self.vchar16, height=1)
        self.text.pack()
        """ funcion que arroja nuestra contraseña generada """
        def passgen():
            gen1 = random.randint(0, 93)
            gen2 = random.randint(0, 93)
            gen3 = random.randint(0, 93)
            gen4 = random.randint(0, 93)
            gen5 = random.randint(0, 93)
            gen6 = random.randint(0, 93)
            gen7 = random.randint(0, 93)
            gen8 = random.randint(0, 93)
            gen9 = random.randint(0, 93)
            gen10 = random.randint(0, 93)
            gen11 = random.randint(0, 93)
            gen12 = random.randint(0, 93)
            gen13 = random.randint(0, 93)
            gen14 = random.randint(0, 93)
            gen15 = random.randint(0, 93)
            gen16 = random.randint(0, 93)

            r1 = self.letters[gen1]
            r2 = self.letters[gen2]
            r3 = self.letters[gen3]
            r4 = self.letters[gen4]
            r5 = self.letters[gen5]
            r6 = self.letters[gen6]
            r7 = self.letters[gen7]
            r8 = self.letters[gen8]
            r9 = self.letters[gen9]
            r10 = self.letters[gen10]
            r11 = self.letters[gen11]
            r12 = self.letters[gen12]
            r13 = self.letters[gen13]
            r14 = self.letters[gen14]
            r15 = self.letters[gen15]
            r16 = self.letters[gen16]
            self.text.insert(1.0, self.letters[gen1]+self.letters[gen2]+self.letters[gen3]+self.letters[gen4]+self.letters[gen5]+self.letters[gen6]+self.letters[gen7]+self.letters[gen8]+self.letters[gen9]+self.letters[gen10]+self.letters[gen11]+self.letters[gen12]+self.letters[gen13]+self.letters[gen14]+self.letters[gen15]+self.letters[gen16])
            self.text.config(state="disabled")
            self.label1.config(text="Contraseña generada: ")
            self.label.config(text=self.letters[gen1]+self.letters[gen2]+self.letters[gen3]+self.letters[gen4]+self.letters[gen5]+self.letters[gen6]+self.letters[gen7]+self.letters[gen8]+self.letters[gen9]+self.letters[gen10]+self.letters[gen11]+self.letters[gen12]+self.letters[gen13]+self.letters[gen14]+self.letters[gen15]+self.letters[gen16])
        self.boton = Button(self.vchar16, text="Generar Password", command=passgen).pack()
        self.vchar16.mainloop()
#creamos las funciones para cada boton.
""" funcion que destruye la ventana raiz y crea otra para nuestro generador de 12 caracteres """
def char12():
    root.destroy()
    ch12 = Char12()

""" funcion que destruye la ventana raiz y crea otra para nuestro generador de 16 caracteres """
def char16():
    root.destroy()
    ch16 = Char16()

#label para nuestro titulo en el frame.
l = Label(fr, text="// Pass Generator //").pack()

#creamos los botones para nuestras funciones del programa.
b1 = Button(fr, text="Generar Pass 12 caracteres", width="25", fg="BLUE", command=char12).pack()
b2 = Button(fr, text="Generar pass 16 caracteres", width="25", fg="GREEN", command=char16).pack()

root.mainloop()

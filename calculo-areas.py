#coding: utf8
#shah sawar
#01/03/2018
import os
os.system ("clear")
from math import pi

print """
                   Calculo de Áreas"""
print"""
a)Triángulo
b)Círculo
"""
menu=raw_input("¿Qué figura quiere calcular (Escriba T o C)?: ")

if (menu !="T") and (menu !="C"):
    print "Introduzca solo (T o C) "
elif menu == "T":
    base=input("Escriba la base: ")
    altura=input("Escriba la altura: ")
    area=input ((base * altura)/2)
    print "Un tringulo de base",base,"y altura",altura,"tiene una area de",area
    
    if (base < 0) or (altura < 0):
        print "No son posibles números menores que cero"
elif menu == "C":
	radio=input("Escriba el radio ")
	print "Un circulo de radio",radio,"tiene un area de",{3.141592654 * radio**2}

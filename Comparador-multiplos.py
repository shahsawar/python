# coding: utf-8
# Shah Sawar
# Fecha 24/02/2018

import os
os.system("clear")

print """

                     COMPARADOR DE MULTIPLOS

 """

num1=input("Introduzca un numero: ")
num2=input("Introduzca otro numero: ")

if (num1==0) or (num2==0):
	print "Error: No se puede multiplicar por 0"
	print "\n"

elif num1>num2:
	mayor=num1
	menor=num2
	
else:
	mayor=num2
	menor=num1
		
if (mayor%menor)==0:
	print mayor,"Es multiplo de ",menor
	
else:
	print mayor,"No es multiplo de ",menor
		

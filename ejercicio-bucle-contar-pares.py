"""
coding:utf-8
shah sawar
05/03/2018
"""

#Inicializaciones
salir="N"
numero=1
amo=input("Introduzca un numero: ")

while (salir=="N"):
       #Hago cosas
       if (numero %2==0):
           print numero
       #Incremento
       numero=numero + 1
       #Activo indicador de salida si toca
       
       if (numero > amo):#Condicion salida
           salir="S"

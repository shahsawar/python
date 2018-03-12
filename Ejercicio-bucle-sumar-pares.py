"""
coding:utf-8
shah sawar
05/03/2018
"""
#Inicializaciones
salir="N"
numero=1

while (salir=="N"):
       #Hago cosas
       if numero%2==0:
           print numero
       #Incremento
       numero=numero + 1
       #Activo indicador de salida si toca
       if (numero>5):#Condicion salida
		    print numero
		     
		    salir="S"

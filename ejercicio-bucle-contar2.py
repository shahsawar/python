# coding:utf-8

#Inicializaciones
salir= "N"
numero=1
amo=input("Introduzca un numero: ")

while (salir=="N"):
       #Hago cosas
       print numero
       #Incremento
       numero= numero + 1
       #Activo indicador de salida si toca
       
       if (numero > amo):#Condicion salida
           salir="S"

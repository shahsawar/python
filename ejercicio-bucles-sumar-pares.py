"""
coding:utf-8
shah sawar
05/03/2018
"""
#Inicializaciones
salir="N"
numero=1
maximo=10
suma=0
while (salir=="N"):
       #Hago cosas
        if numero%2==0:
            print numero,
        
        
            if (numero<=maximo -2):
                print "+",
        
            suma=suma+numero
        
       #Incremento
        numero=numero + 1
       #Activo indicador de salida si toca
        if (numero>maximo):#Condicion salida
            salir="S"
print "=",suma

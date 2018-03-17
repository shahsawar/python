"""coding:utf-8
shah sawar
15/03/2018
"""

# Inicializaciones
salir = "N"
numero=1
maximo=5
suma=0
while ( salir=="N" ):
    # Hago cosas
    print numero,
    
    if (numero<=maximo -1):
        print "+",
    suma=suma + numero
    # Incremento
    numero=numero + 1
    # Activo indicador de salida si toca
    if (numero > maximo): # Condicion de salida
            salir = "S"

print "=",suma

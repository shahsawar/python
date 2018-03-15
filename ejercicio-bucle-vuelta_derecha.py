"""
coding: utf-8
shah sawar
ejercicio-bucle-vuelta_derecha.py
"""
# Inicializaciones
salir = "N"
vuelta=1
maximo=8
while ( salir=="N" ):
    # Hago cosas
    if (vuelta%8==1) or (vuelta%8==2):
        print (vuelta,"->Arriba")
    
    if (vuelta%8==3) or (vuelta%8==4):
        print (vuelta,"->Derecha")
    
    if (vuelta%8==5) or (vuelta%8==6):
        print (vuelta,"->Abajo")
        
    if (vuelta%8==7) or (vuelta%8==0):
        print (vuelta,"->Izquierda")
        
    # Incremento
    vuelta=vuelta + 1
    # Activo indicador de salida si toca
    if (vuelta > maximo ): # Condicion de salida
            salir = "S"
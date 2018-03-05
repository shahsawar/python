#coding:utf8
#shah sawar
#03/03/2018

import os
os.system("clear")

print """

               ······································ 
               ··                                  ··
               ··  CONVERTIDOR DE CM A KM, M Y CM  ··
               ··                                  ··
               ······································ """
print ("\n")

centimetros = int(input("Escriba una distancia en centímetros: "))

kilometros = centimetros // 100000
metros = centimetros % 100000 // 100
resto = centimetros % 100

print centimetros,"centímetros son",kilometros,"km",metros,"m",resto,"cm"

# coding: utf-8
# shah sawar
# 28/2/2018

import os
os.system("clear")

year=input("Escriba un año cualquier:  ")

#Si el año es multiplo 4 y no de 100 == No es bisiesto
if (year % 100 == 0):
    print "El año",year,"No es bisiesto"

#Si el año es multiplo de 4 y de 100 ==Es bisiesto
else:
	if (year % 4 == 0) or (year % 400 == 0):
         print "El año",year,"Si es bisiesto"

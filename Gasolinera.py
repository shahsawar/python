# coding: utf-8
# Shah sawar
# 23/02/2018

import os
os.system ("clear")

print """
		#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
		#                                       #
		#          WELCOME TO GAS STATION       #
		#                                       #
		#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
		*****************************************
		**       >>>>>   1)SUPER      <<<<<    **
		**                                     **
		**       >>>>>   2)SIN PLOMO  <<<<<    **
		**                                     **
		**       >>>>>   3)DIESEL     <<<<<    **
		***************************************** """
print "\n"
print  ("                      Elige un tipo de gasolina")
print "\n"

Numero1=input ("Selecciona un numero: ")

if Numero1<=0 or Numero1>3:
	print "Perdona!Esta opcion no esta en la lista "

elif Numero1==1:
	print """
		*********************************
		**                             **
		**   1)Super_Normal  (1.5€)    **
		**   2)Super_Turbo   (1.55€)   **
		**                             **
		**                             **
		********************************* """
	print "\n"
	
	numero1=input ("Selecciona un numero: ")
	
	if numero1==1:
	   
	    normal= 1.5
	    cantidad=input("Introduzca la cantidad de litros: ")
	    precio=normal * cantidad
	    
	    print "Su Importe Total de Super Normal es ",precio," €"
	    
	elif numero1==2:
	   
	    turbo= 1.55
	    cantidad=input("Introduzca la cantidad de litros: ")
	    precio=turbo * cantidad
	    
	    print "Su Importe Total de Super Turbo es ",precio," €"
	    
	else:
		print ("Error:Esta opcion no esta en la lista")




if Numero1==2:
	print """
		****************************************
		**                                    **
		**    1)Sin plomo_Normal (1.6€)       **
		**    2)Sin plomo_Con aditivo(1.65€)  **
		**                                    **
		**                                    **
		**************************************** """
	print "\n"
	
	numero2=input ("Selecciona un numero: ")
	
	if numero2==1:
	   
	    normal= 1.6
	    cantidad=input("Introduzca la cantidad de litros: ")
	    precio=normal * cantidad
	    
	    print "Su Importe Total de Sin Plomo Normal Normal es ",precio," €"
	    
	elif numero2==2:
	   
	    aditivo= 1.65
	    cantidad=input("Introduzca la cantidad de litros: ")
	    precio=aditivo * cantidad
	    
	    print "Su Importe Total de Sin Plomo Con Aditivos es",precio," €"
	    
	else:
		print ("Error:Esta opcion no esta en la lista")
		

if Numero1==3:
	print """
		****************************************
		**                                    **
		**    1)Diesel_Normal (1.7€)          **
		**    2)Diesel_Fast&Furius(1.75€)     **
		**                                    **
		**                                    **
		**************************************** """
	print "\n"
	
	numero3=input ("Selecciona un numero: ")
	
	if numero3==1:
	   
	    normal= 1.7
	    cantidad=input("Introduzca la cantidad de litros: ")
	    precio=normal * cantidad
	    
	    print "Su Importe Total de Diesel Normal es ",precio," €"
	    
	elif numero3==2:
	   
	    fast= 1.75
	    cantidad=input("Introduzca la cantidad de litros: ")
	    precio=fast * cantidad
	    
	    print "Su Importe Total de Diesel Fast&Furius es",precio," €"
	    
	else:
		print ("Error:Esta opcion no esta en la lista")

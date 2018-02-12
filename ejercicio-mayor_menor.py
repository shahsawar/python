valorA=input("Introduzca valor A ")
valorB=input("Introduzca valor B ")
valorC=input("Introduzca valor C ")

if (valorA==valorB) and (valorA==valorC):
    print ("ERROR: Hay 3 valores iguales")
else:
	if (valorA>valorB) and (valorB>valorC):
		print ("valorA es mayor")
		print ("valorC es menor")
	else:
		if (valorA>valorC) and (valorC>valorB):
			print ("valorA es mayor")
			print ("valorB es menor")
		else:
			if (valorB>valorC) and (valorC>valorA):
				print ("valorB es mayor")
				print ("valorA es menor")
			else:
				if (valorB>valorA) and (valorB>valorC):
					print ("valorB es mayor")
					print ("valorC es menor")
				else:
					if (valorC>valorB) and (valorB>valorA):
						print ("valorC es mayor")
						print ("valorA es menor")
					else:
						if (valorC>valorA) and (valorA>valorB):
							print ("valorC es mayor")
							print ("valorB es menor")
						else:
						    print ("ERROR: Hay 2 valores iguales")

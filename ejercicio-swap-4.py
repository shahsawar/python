#conding: utf-8
#Shah Sawar
#Ejercicio-swap-4.py

print ("""          
      <*>Introduzca 4 Cosas Diferente<*>
      
      Por ejemplo:(el resultado seria asi)
      
         Antes                    Despues
      Cajon1="Movil"           Cajon1="Boli" 
      Cajon2="Bocadillo"       Cajon2="Bebida"
      Cajon3="Boli"            Cajon3="Movil"
      Cajon4="Bebida"          Cajon4="Bocadillo"
   """)

Cajon1=raw_input ("Introduzca Cajon1 ")
Cajon2=raw_input ("Introduzca Cajon2 ")
Cajon3=raw_input ("Introduzca Cajon3 ")
Cajon4=raw_input ("Introduzca Cajon4 ")

Cajon_Extra=Cajon1
Cajon1=Cajon2
Cajon2=Cajon3
Cajon3=Cajon4
Cajon4=Cajon_Extra
Cajon4=Cajon_Extra

Cajon_Extra=Cajon1
Cajon1=Cajon2
Cajon2=Cajon3
Cajon3=Cajon4
Cajon4=Cajon_Extra
Cajon4=Cajon_Extra


print ("""          

       >>>RESULTADO FINAL<<<
   """)
print ("ahora el Cajon1 tiene="),Cajon1
print ("ahora el Cajon2 tiene="),Cajon2
print ("ahora el Cajon3 tiene="),Cajon3
print ("ahora el Cajon4 tiene="),Cajon4

print ("""          
           <<<Adios!!!>>>
   """)



#Programa para determinar una selección aleatoria entre los elementos de una lista

#Developer: Botta, Teo Mariano

#Version: 1.0

import random	#Librería que contine función de random
import os		#Librería que contiene función de limpiar pantalla

os.system('clear')	#Limpio pantalla al iniciar la ejecución del programa	
l = ["Agustín", "Félix", "Martín", "Matias", "Teo"]	#Defino la lista que contiene el nombre a imprimir
a = random.randint(0,4)	#Le asigno a 'a' un valor aleatorio entre 0 y 4
print(l[a])	#Imprimo el valor correspondiente a la lista en la posición 'a'
input()	#Espero que se presione alguna tecla antes de continuar la ejecución
os.system('clear')	#Función de limpiado de pantalla
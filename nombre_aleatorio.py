#Programa para determinar una selección aleatoria entre los elementos de una lista.

#Developer: Botta, Teo Mariano

#Version: 1.0

#Version: 2.0
#Se incorpora funcionalidad en la cantidad de ocurrencias. Se debe llegar a tres ocurrencias.

import random	#Librería que contine función de random
import os		#Librería que contiene función de limpiar pantalla

os.system('clear')	#Limpio pantalla al iniciar la ejecución del programa	
l = ["Agustín", "Félix", "Martín", "Matias", "Teo"]	#Defino la lista que contiene el nombre a imprimir
v = [0, 0, 0, 0, 0]
s = 1
while(s == 1):
	r = random.randint(0,4)	#Le asigno a 'r' un valor aleatorio entre 0 y 4
	if(r == 0):
		v[0]+=1	#Se aumenta en una unidad el contador en la posición correspondiente
		if(v[0] == 3):	
			s = 0	#Si alguno llega a 3 ocurrencias, se termina el sorteo cambiando el estado de 's'
	elif(r == 1):
		v[1]+=1
		if(v[1] == 3):
			s = 0
	elif(r == 2):
		v[2]+=1
		if(v[2] == 3):
			s = 0
	elif(r == 3):
		v[3]+=1
		if(v[3] == 3):
			s = 0
	elif(r == 4):
		v[4]+=1
		if(v[4] == 3):
			s = 0
for x in range(0,5):	
	print(l[x]+":"+str(v[x]))	#Imprimo ambas listas, mostrando el nombre junto con su cantidad de ocurrencias
print()
print("Hoy le toca pasar lista a: "+l[r])	#Imprimo el valor correspondiente a la lista en la posición 'r'
input()	#Espero que se presione alguna tecla antes de continuar la ejecución
os.system('clear')	#Función de limpiado de pantalla
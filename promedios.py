# Developer: Botta, Teo Mariano

# Versión: 1.0

#El siguiente programa realiza un promedio de las notas ingresadas por teclado. Las cuales pueden ser una cantidad indefinida.



import os	#Importo librería que permite función de limpiado de pantalla
from cmprom import * #Invoco librería 'cmprom' para utilizar la clase 'Materia'

os.system('clear')	#Limpio la consola al comienzo de la ejecución
p = 0	#Inicializo variable de acumulación 
l = []	#Inicializo una lista en la cual se irán ingresando las notas a promediar
r = input('Agregar nota? (s/n): ')	#Se solicita confirmación inicial a la carga de notas
while(r == 's'):	#Se realiza la iteración mientras la variable 'r' sea igual a 's'
	os.system('clear')	#Limpi pantalla
	m = input('Ingrese materia: ')	#Solicito materia
	print('')
	n = input('Ingrese nota: ')	#Solicito nota
	mate = Materia(m,n)	#Instancio una clase de tipo 'Materia'
	l.append(mate)	#Agrego la instancia 'mate' al final de la lista 'l'
	print('-----------------------')
	r = input('Agregar otra nota? (s/n): ')	#Se solicita confirmación de continuidad
c = 0	#Inicializo una variable contador
os.system('clear')	#Limpio pantalla
print('Listado de notas:')
for x in l:	#Recorro todos los elementos de la lista
	p = p + int(x.verNota())	#Voy sumando los valores de cada nota en la variable 'p'
	c = c + 1	#Aumento la variable contador
	print('Materia: '+ str(x.verNombre()))	#Imprimo valores invocando funciones de la clase 'Materia' 
	print('Nota: '+ str(x.verNota()))	#Imprimo valores invocando funciones de la clase 'Materia'
	print('----------------------------------')
if(c != 0):
	p = p / c 	#Realizo el promedio de las notas y las guardo en la variable 'p'
	print('El promedio de las notas es de: ',float(p))	#Imprimo en consola el promedio
else: 
	print('No hay notas cargadas.')	#Muestro mensaje de ausencia de datos
print('-------------------------------------')
input('Presione cualquier tecla para finalizar...')	#Solicito presión de cualquier tecla antes de finalizar
os.system('clear')	#Limpio pantalla antes de finalizar
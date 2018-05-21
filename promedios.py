# Developer: Botta, Teo Mariano

# Versión: 1.0

#El siguiente programa realiza un promedio de las notas ingresadas por teclado. Las cuales pueden ser una cantidad indefinida.

# Versión: 2.0
#Se agrega Menú inicial y función de iteración para el control del mismo

# Versión: 2.1
#Se agrega oción de cancelamiento de cargas

# Versión: 2.2
#Se corrige bug de error de cálculos


import os	#Importo librería que permite función de limpiado de pantalla
from cmprom import * #Invoco librería 'cmprom' para utilizar la clase 'Materia'

os.system('clear')	#Limpio la consola al comienzo de la ejecución
p = 0	#Inicializo variable de acumulación 
l = []	#Inicializo una lista en la cual se irán ingresando las notas a promediar
o = 9	#Inicializo la variable 'o' en '9' para que ingrese distinta a '0'
c = 0	#Inicializo una variable contador
while(o != 0):	#Mientras se cumpla la condición, muestro menú
	print('1-Agregar notas')
	print('2-Mostrar notas')
	print('0-Salir')
	o = input('Ingrese opción a realizar: ')
	if(o == '1'):	#Si la opción elegida es '1', paso a solicitar ingreso de materias
		r = 's'	#Seteo 'r' con el valor 's' para entrar al WHILE
		while(r == 's'):	#Se realiza la iteración mientras la variable 'r' sea igual a 's'
			os.system('clear')	#Limpi pantalla
			print('Si desea cancelar la carga actual, ingrese "xxx" como materia')
			print()
			m = input('Ingrese materia: ')	#Solicito materia
			if(m != 'xxx'):	#Mediante este ingreso, se puede cancelar la carga de materias
				print('')	#Línea en blanco a fines estéticos en la consola
				n = input('Ingrese nota: ')	#Solicito nota
				mate = Materia(m,n)	#Instancio una clase de tipo 'Materia'
				l.append(mate)	#Agrego la instancia 'mate' al final de la lista 'l'
				print('-'*40)	#Línea de separación
				r = input('Agregar otra nota? (s/n): ')	#Se solicita confirmación de continuidad
			else:
				break
		p = 0	#Reinizializo 'p'. De esta forma evito acumulación en cada iteración de las cargas
		c = 0	#Reinizializo 'c'. De esta forma evito acumulación en cada iteración de las cargas
		for x in l:	#Recorro todos los elementos de la lista
			p = p + int(x.verNota())	#Voy sumando los valores de cada nota en la variable 'p'
			c = c + 1	#Aumento la variable contador
		if(c != 0):	#Verifico que se pueda realizar el cálculo
			p = p / c 	#Realizo el promedio de las notas y las guardo en la variable 'p'
		os.system('clear')	#Limpio pantalla
	elif(o == '2'):	#Si la opción es '2', paso a verificar si hay notas cargadas y su muestreo
		if(c != 0):
			print()
			print('Listado de notas:')
			print()
			for x in l:	#Recorro todos los elementos de la lista
				print('Materia: '+ str(x.verNombre()))	#Imprimo valores invocando funciones de la clase 'Materia' 
				print('Nota: '+ str(x.verNota()))	#Imprimo valores invocando funciones de la clase 'Materia'
				print('-'*40)
			print('El promedio de las notas es de: ',float(p))	#Imprimo en consola el promedio
			print()
			print('Presione cualquier tecla para continuar...')
			input()	#Espero confirmación para luego limpiar pantalla
			os.system('clear')
		else:
			print()
			print('No hay notas cargadas.')	#Muestro mensaje de ausencia de datos
			print('-'*40)
			print('Presione cualquier tecla para continuar...')
			input()	#Espero confirmación para luego limpiar pantalla
			os.system('clear')
	elif(o == '0'):	#Si la opción es '0', corto la iteración y cierro la aplicación
		print()
		break
	else:
		print()
		print('Opción inválida. Presione cualquier tecla para continuar...')
		input()
		os.system('clear')
input('Presione cualquier tecla para finalizar...')	#Solicito presión de cualquier tecla antes de finalizar
os.system('clear')	#Limpio pantalla antes de finalizar

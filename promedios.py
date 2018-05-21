# Developer: Botta, Teo Mariano

# Versión: 1.0

#El siguiente programa realiza un promedio de las notas ingresadas por teclado. Las cuales pueden ser una cantidad indefinida.

# Versión: 2.0
#Se agrega Menú inicial y función de iteración para el control del mismo

# Versión: 2.1
#Se agrega oción de cancelamiento de cargas

# Versión: 2.2
#Se corrige bug de error de cálculos

# Versión: 3.0
#Se agrega opción de eliminación de materias cargadas
#Se optimiza el uso de ciertos comandos para ahorrar líneas de código

import os	#Importo librería que permite función de limpiado de pantalla
from cmprom import * #Invoco librería 'cmprom' para utilizar la clase 'Materia'

l = []	#Inicializo una lista en la cual se irán ingresando las notas a promediar
o = 9	#Inicializo la variable 'o' en '9' para que ingrese distinta a '0'
while(o != 0):	#Mientras se cumpla la condición, muestro menú
	os.system('clear')	#Limpio la consola al comienzo de la ejecución
	p = 0	#Inicializo variable de acumulación. Se inicializa dentro del loop para evitar redundancia de datos
	c = 0	#Inicializo una variable contador. Se inicializa dentro del loop para evitar redundancia de datos
	print('1-Agregar notas')
	print('2-Mostrar notas')
	print('3-Eliminar nota')
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
	elif(o == '2'):	#Si la opción es '2', paso a verificar si hay notas cargadas y su muestreo
		os.system('clear')
		for x in l:	#Recorro todos los elementos de la lista
			p = p + int(x.verNota())	#Voy sumando los valores de cada nota en la variable 'p'
			c = c + 1	#Aumento la variable contador
		if(c != 0):	#Verifico que se pueda realizar el cálculo
			p = p / c 	#Realizo el promedio de las notas y las guardo en la variable 'p'
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
		else:
			print()
			print('No hay notas cargadas.')	#Muestro mensaje de ausencia de datos
			print('-'*40)
			print('Presione cualquier tecla para continuar...')
			input()	#Espero confirmación para luego limpiar pantalla
	elif(o == '3'):	#Si la opción seleccionada es '3', paso solicitar materia a eliminar
		le = []	#Inicializo lista que contendrá solamente los nombres de las materias
		os.system('clear')
		print('Materias cargadas actualmente:')
		print()
		if(len(l) == 0):	#Verifico que haya materias cargadas. Caso negativo, indico con mensaje en pantalla
			print('No hay materias cargadas. Presione cualquier tecla para continuar...')
		else:
			for x in l:
				print(str(x.verNombre()))	#Muestro las materias cargadas en la lista original
				le.append(x.verNombre())	#Inserto en 'le' el nombre de las materias cargadas
			print('-'*40)
			e = input('Ingrese nombre de la materia a eliminar: ')	#Solicito materia a eliminar
			print()
			if(e in le):	#Verifico la existencia de la materia 'e' en la lista
				for x in l:	
					if(e == x.verNombre()):	#Busco la materia en la lista original y la elimino
						l.remove(x)	#Elimino el objeto tipo MATERIA 'x' de la lista original
						print('La materia ',str('"'+e+'"'),' ha sido eliminada. Presione cualquier tecla para continuar...')	#Muestro mensaje de borrado
			else:
				print('La materia ',str('"'+e+'"'),' no está cargada. Presione cualquier tecla para continuar...')	#Indico si la materia no está cargada		
		input()
	elif(o == '0'):	#Si la opción es '0', corto la iteración y cierro la aplicación
		print()
		break
	else:
		print()
		print('Opción inválida. Presione cualquier tecla para continuar...')
		input()
input('Presione cualquier tecla para finalizar...')	#Solicito presión de cualquier tecla antes de finalizar
os.system('clear')	#Limpio pantalla antes de finalizar

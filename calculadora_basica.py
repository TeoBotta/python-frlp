#Este programa simula una calculadora básica. Solicita dos números, un operador y luego muestra el esquema de la operación y su resultado.
#Así mismo, el proceso se realiza dentro de un loop, con el fin de no abrir el progama por cada cuenta a realizar.
#Version: 1.0

#Developer: Botta, Teo Mariano

#Version: 2.0
#Se incorpora función de muestra sobre las operaciones realizadas.

import os #Librería para usar el clear(equivalente al clrscr)

os.system('clear')	#Limpio pantalla de la consola antes de iniciar
print("Bienvenido a calculadora básica.")
print("--------------------------------")
print("")
s = 1	#Establezco 's' en '1' para que entre al WHILE por defecto
l = []  #Creo una lista vacía en 'l'. Los valores se irán agregando durante la ejecución
while(s == 1):
	n1 = input("Ingrese operador: ") #Solicito operadores y operación
	print("")
	n2 = input("Ingrese operando: ")
	print("")
	op = input("Ingrese operación: ")
	print("")
	print("----------------------------")
	print("")
	#Convierto a tipo de dato integer. De esta forma puedo operar con 'a' y 'b' como integers
	a = int(n1)
	b = int(n2)
	if(op == '+'):
		res = a + b #Opero con los tipos integer
		print("El resultado de " + n1 + " + " + n2 + " es: " + str(res)) #Muestro resultado imprimiendo 'res' como STRING porque está concatenando
		c = str(n1+'+'+n2+'='+str(res)) #Genero 'c' para guardar el equema de la operación
		l.append(c) #Guardo el esquema de la operación en la lista 'l'
	elif(op == '-'):
		res = a - b
		print("El resultado de " + n1 + " - " + n2 + " es: " + str(res))
		c = str(n1+'-'+n2+'='+str(res))
		l.append(c)
	elif(op == '*'):
		res = a * b
		print("El resultado de " + n1 + " * " + n2 + " es: " + str(res))
		c = str(n1+'*'+n2+'='+str(res))
		l.append(c)
	elif(op == '/'):
		if(b != 0): #Verifico que no se pueda dividir por cero
			res = a / b
			print("El resultado de " + n1 + " / " + n2 + " es: " + str(res))
			c = str(n1+'/'+n2+'='+str(res))
			l.append(c)
		else:
			print("No se puede divir por cero...")
	else:
		print("Operador no válido...")
	print("---------------------------------")
	print("")
	r = input("Desea realizar otra operación? (s/n) ") #Pregunto si hay más operaciones a realizar
	#Si la respuesta es distinta a 's', seteo valor de la variable 's' para que no ingrese al WHILE nuevamente
	if(r != 's'):
		s = 0
	os.system('clear')  #Función de la librería 'os'. OJO: en windows se usa os.system('cls')
print("A continuación se listan las operaciones resueltas en ésta sesión:")
print("---------------------")
for x in l: print(x)	#Imprimo los esquemas guardados previamente
print("---------------------")
input("Presione cualquier tecla para finalizar...") #Espero orden de continuidad para cerrar el programa
os.system('clear') #Limpio pantalla de la consola antes de finalizar
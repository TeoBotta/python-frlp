#Este programa simula una calculadora básica. Solicita dos números, un operador y luego muestra el esquema de la operación y su resultado.
#Así mismo, el proceso se realiza dentro de un loop, con el fin de no abrir el progama por cada cuenta a realizar.

#Developer: Botta, Teo Mariano
#Version: 1.0


import os #Librería para usar el clear(equivalente al clrscr)

os.system('clear')
print("Bienvenido a calculadora básica.")
print("--------------------------------")
print("")
s = 1
while(s == 1):
	n1 = input("Ingrese operador: ")
	print("")
	n2 = input("Ingrese operando: ")
	print("")
	op = input("Ingrese operación: ")
	print("")
	print("----------------------------")
	print("")
	a = int(n1) #Convierto a tipo de dato integer
	b = int(n2) #Convierto a tipo de dato integer
	if(op == '+'):
		res = a + b #Opero con los tipos integer
		print("El resultado de " + n1 + " + " + n2 + " es: " + str(res)) #Muestro resultado imprimiendo 'res' como STRING porque está concatenando
	elif(op == '-'):
		res = a - b
		print("El resultado de " + n1 + " - " + n2 + " es: " + str(res))
	elif(op == '*'):
		res = a * b
		print("El resultado de " + n1 + " * " + n2 + " es: " + str(res))
	elif(op == '/'):
		if(b != 0):
			res = a / b
			print("El resultado de " + n1 + " / " + n2 + " es: " + str(res))
		else:
			print("No se puede divir por cero...")
	else:
		print("Operador no válido...")
	print("---------------------------------")
	print("")
	r = input("Desea realizar otra operación? (s/n) ")
	if(r != 's'):
		s = 0
	os.system('clear')  #Función de la librería 'os'. OJO: en windows se usa os.system('cls')
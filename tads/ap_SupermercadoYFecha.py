from tadProducto import *
from tadSupermercado import *
from datetime import datetime, date, time


#Crea el supermercado
super=crearSupermercado()

#Cargar el curso
rta = 's'
while rta == 's':
	p=crearProducto()
	c=int(input("Ingrese un codigo "))
	l=int(input("Ingrese un precio "))
	p=input("Ingrese un nombre ")
	isValidDate = False
	while isValidDate == False:
		fecha=input("Ingrese fecha de vencimiento del producto. Formato: dd/mm/yyyy")
		day,month,year = fecha.split('/')
		if len(year) == 4 and len(month) == 2 and len(day) == 2:
			fecha = date(int(year),int(month),int(day))
			isValidDate = True

	
	cargarProducto(p,c,l,p,fecha)
	agregarProducto(super,p)
	rta = input("Ingresa otro alumno?s/n")

#Imprime los productos vencidos  

tam=tamanio(super)
print("Los productos vencidos son:")
for i in range(0,tam):
	a=recuperarProducto(super,i)
	if verVto(i) < datetime.today():
	
		print(verCodigo(p))
		print(verPrecio(p))
		print(verNombre(p))
		print(verFecha(p))
	print('__________'*3)

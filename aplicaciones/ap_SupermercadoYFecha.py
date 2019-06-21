from tadProducto import *
from tadSupermercado import *
from datetime import datetime, date, time


#Crea el supermercado
super=crearSupermercado()
formato = "%d/%m/%Y"
#Cargar el curso
rta = 's'
while rta == 's':
	p=crearProducto()
	c=int(input("Ingrese un codigo "))
	l=int(input("Ingrese un precio "))
	nom=input("Ingrese un nombre ")
	isValidDate = False
	while isValidDate == False:
		try:
			fecha=input("Ingrese fecha de vencimiento del producto. Formato: dd/mm/yyyy: ")
			day,month,year = fecha.split('/')
			if len(year) == 4 and len(month) == 2 and len(day) == 2 and int(year) > 2000 and int(year) < 2050:
				fecha = date(int(year),int(month),int(day))
				isValidDate = True

		except ValueError:
			print("Fecha incorrecta. Ingresela nuevamente.")
			isValidDate = False



	cargarProducto(p,c,l,nom,datetime.strftime(fecha, formato))
	agregarProducto(super,p)
	rta = input("Ingresa otro alumno?s/n")

#Imprime los productos vencidos

tam=tamanio(super)
print("Los productos vencidos son:")
for i in range(0,tam):
	a=recuperarProducto(super,i)
	fechaActual= datetime.strptime(verVto(a), formato)
	if fechaActual < datetime.today():

		print(verCodigo(p))
		print(verPrecio(p))
		print(verNombre(p))
	print('__________'*3) 
# -*- coding: cp1252 -*-
import TadAluFecha,datetime

from TadAluFecha import *

#Crea y carga los datos del alumno1
a1=crearAlu()
n=input("Ingrese un nombre ")
l=input("Ingrese un legajo ")
p=input("Ingrese un promedio ")
print("Especifique fecha de ingreso")
d=input('día de ingreso')
m=input('mes de ingreso, numérico')
a=input('Año de ingreso')
f=date(int(a),int(m),int(d))
cargarAlu(a1,n,l,p,f)

#Imprime los datos del alumno1
print('*********************************')
print(verNom(a1))
print(verLega(a1))
print(verProm(a1))
print(verFecha(a1))
print('*********************************')

#Crea y carga los datos del alumno2
a2=crearAlu()
n=input("Ingrese un nombre ")
l=input("Ingrese un legajo ")
p=input("Ingrese un promedio ")
print("Especifique fecha de ingreso")
d=input('día de ingreso')
m=input('mes de ingreso, numérico')
a=input('Año de ingreso')
f=date(int(a),int(m),int(d))
cargarAlu(a2,n,l,p,f)

#Imprime los datos del alumno1

print('*********************************')
print(verNom(a2))
print(verLega(a2))
print(verProm(a2))
print(verFecha(a2))
print('*********************************')

#Imprime el nombre del alumno de menor legajo
print("El nombre del alumno de menor promedio es:")
if (verProm(a1)<verProm(a2)):
    print(verNom(a1))
else:
    print(verNom(a2))
print('*********************************')
#Modifica el promedio del alumno1
p=input("Ingrese un promedio para modificar al alumno 1 ")
modiProm(a1,p)
print(verNom(a1))
print(verLega(a1))
print(verProm(a1))
print(verFecha(a1))
x=input('presione una tecla para continuar')
print('*********************************')
anio1=verFecha(a1)
anio2=verFecha(a2)
if anio1.year > anio2.year:
    print('El primer alumno ingresó después que el 2do')
else:
    print('el segundo alumno entró después')
x=input('presione una tecla para continuar')
print('*********************************')
asignarAlu(a1,a2)#Asigna los datos de a2 en a1
print("Imprime los datos del alumno1 luego de la asignacion")
print(verNom(a1))
print(verLega(a1))
print(verProm(a1))
print(verFecha(a1))
print("Imprime los datos del alumno2")
print(verNom(a2))
print(verLega(a2))
print(verProm(a2))
print(verFecha(a2))
x=input()


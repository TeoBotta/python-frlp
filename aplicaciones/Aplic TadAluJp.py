import TadAlu

from TadAlu import *

#Crea y carga los datos del alumno1
a1=crearAlu()
n=raw_input("Ingrese un nombre")
l=input("Ingrese un legajo")
p=input("Ingrese un promedio")
cargarAlu(a1,n,l,p)

#Imprime los datos del alumno1
print verNom(a1)
print verLega(a1)
print verProm(a1)

#Crea y carga los datos del alumno2
a2=crearAlu()
n=raw_input("Ingrese un nombre")
l=input("Ingrese un legajo")
p=input("Ingrese un promedio")
cargarAlu(a2,n,l,p)

#Imprime los datos del alumno1
print verNom(a2)
print verLega(a2)
print verProm(a2)

#Imprime el nombre del alumno de menor legajo
print "El nombre del alumno de menor legajo es:"
if (verLega(a1)<verLega(a2)):
    print verNom(a1)
else:
    print verNom(a2)

#Modifica el promedio del alumno1
p=input("Ingrese un promedio")
modiProm(a1,p)
print verProm(a1)
print verNom(a1)
print verLega(a1)
print verProm(a1)

asignarAlu(a1,a2)#Asigna los datos de a2 en a1
print "Imprime los datos del alumno1 luego de la asignacion"
print verNom(a1)
print verLega(a1)
print verProm(a1)
print "Imprime los datos del alumno2"
print verNom(a2)
print verLega(a2)
print verProm(a2)

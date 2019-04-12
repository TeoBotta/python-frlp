# -*- coding: cp1252 -*-
import TadAluFecha, TadCurso

from TadAluFecha import *
from TadCurso import *


#Crea el curso
c=crearCurso()

#Cargar el curso
for i in range(1,4):
    a=crearAlu()
    n=raw_input("Ingrese un nombre ")
    l=input("Ingrese un legajo ")
    p=input("Ingrese un promedio ")
    print("Especifique fecha de ingreso")
    d=input('día de ingreso')
    m=input('mes de ingreso, numérico')
    a=input('Año de ingreso')
    f=date(a,m,d)
    cargarAlu(a,n,l,p,fe)
    agregarAlu(c,a)

#Imprime los datos del curso    
print "Imprime los datos del curso"
tam=len(c)
for i in range(0,tam):
    a=recuperarAlu(c,i)
    print "Imprime los datos de un alumno"
    print verNom(a)
    print verLega(a)
    print verProm(a)
    print verFecha(a)
    print '__________'*3

raw_input('presione una tecla para continuar')

#Recupera e imprime el segundo alumno
print "Imprime los datos del 2do alumno"
a=recuperarAlu(c,1)
print "Imprime los datos de un alumno"
print verNom(a)
print verLega(a)
print verProm(a)
print verFecha(a)

print'********************************'
print "Elimina el alumno recuperado"
#Elimina el alumno recuperado
eliminarAlu(c,a)

#Imprime los alumnos que quedan en el curso
print "Imprime los datos de los alumnos del curso"
tam=len(c) 
for i in range(0, tam):
    a=recuperarAlu(c,i)
    print "Imprime los datos de un alumno"
    print verNom(a)
    print verLega(a)
    print verProm(a)
    print verFecha(a)
    print '                       '
raw_input()

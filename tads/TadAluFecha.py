# -*- coding: cp1252 -*-
# Tad Alu

from datetime import datetime, date, time

#formato = "%d/%m/%Y"

def crearAlu():
    #Crea un alumno vacio
    alumno=["",0,0,0]
    return alumno

def cargarAlu(alumno,n,l,p,fe):
    #Carga los datos de un alumno
    alumno[0]=n
    alumno[1]=l
    alumno[2]=p
    alumno[3]=fe

def verNom(alumno):
    #Retorna el nombre de un alumno
    return alumno[0]

def verLega(alumno):
    #Retorna el legajo de un alumno
    return alumno[1]

def verProm(alumno):
    #Retorna el promedio de un alumno
    return alumno[2]

def verFecha(alumno):
    #Retorna la fecha de ingreso  de un alumno
    #return datetime.strptime(alumno[3], formato)
    return alumno[3]
    

def modiNom(alumno,n):
    #Modifica el nombre de un alumno
    alumno[0]=n

def modiLega(alumno,l):
    #Modifica el legajo de un alumno
    alumno[1]=l

def modiProm(alumno,p):
    #Modifica el promedio de un alumno
    alumno[2]=p

def modiFecha(alumno,fe):
    #Modifica la fecha de ingreso de un alumno
    alumno[3]=fe
    
def asignarAlu(alumno1,alumno2):
    #Asigna los datos de un alumno en otro
    modiNom(alumno1,verNom(alumno2))
    modiLega(alumno1,verLega(alumno2))
    modiProm(alumno1,verProm(alumno2))
    modiFecha(alumno1,verFecha(alumno2))  

# Tad Producto
from datetime import datetime, date, time
#Especificación

def crearProducto(): pass
    #Crea un producto vacio

def cargarProducto(producto,c,p,n,vto): pass
    #Carga los datos de un producto
	
def verCodigo(producto): pass
    #Retorna el codigo de un producto
	
def verPrecio(producto): pass
    #Retorna el precio de un producto
	
def verNombre(producto): pass
    #Retorna el nombre de un producto
	
def modiCodigo(producto,c): pass
    #Modifica el codigo de un producto
	
def modiPrecio(producto,p): pass
    #Modifica el precio de un producto
	
def modiNombre(producto,n): pass
    #Modifica el nombre de un producto
	
def asignarProducto(producto1,producto2): pass
    #Asigna los datos de un producto en otro
	
#Implementación

def crearProducto():
    producto=[0,0,"",""]
    return producto
	
	



def cargarProducto(producto,c,p,n,vto):
	producto[0]=c
	producto[1]=p
	producto[2]=n
	producto[3]=vto

def verCodigo(producto):
    return producto[0]

def verPrecio(producto):
    return producto[1]

def verNombre(producto):
    return producto[2]

def modiCodigo(producto,c):
    producto[0]=c

def modiPrecio(producto,p):
    producto[1]=p

def modiNombre(producto,n):
    producto[2]=n
	
def verVto(producto):
	return producto[3]
	
def asignarProducto(producto1,producto2):
    modiNom(producto1,verNom(producto2))
    modiLega(producto1,verLega(producto2))
    modiProm(producto1,verProm(producto2))

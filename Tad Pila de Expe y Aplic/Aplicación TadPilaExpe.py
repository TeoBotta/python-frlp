import TadExpediente, TadPila

from TadExpediente import *
from TadPila import *


p=crearPila()
paux=crearPila()
#Carga la Pila original
print("Carga datos en la pila")
for i in range (1,5):
    e=crearExpe()
    n=input("Ingrese un numero")
    t=input("Ingrese un tipo de expediente")
    cargarExpe(e,n,t)
    apilar(p,e)   

#Imprime la Pila original   
print("Imprime los datos de la pila")
for i in range (0, tamanio(p)):
    elem=desapilar(p)
    apilar(paux,elem)
    print(elem)
    
#Ojo!! para imprimir la pila hay que ir recuperando los datos pero para probar
#Prueba no hacer, muestra que quedo la pila original vacia y la auxiliar con datos
print("pila original y auxiliar")
print(p)
print(paux)

#pasamos los datos de la pila auxiliar a la original
copiarPila(p,paux)
print("pila original y auxiliar despues del copiarpila")
#Prueba no hacer, muestra que quedo la pila original tiene los datos y la auxiliar esta vacia
print(p)
print(paux)

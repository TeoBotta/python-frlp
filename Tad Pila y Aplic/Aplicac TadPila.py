import TadPila

from TadPila import *

p=crearPila()
paux=crearPila()

print ("Carga datos en la pila")
for i in range (1,5):
    elem=input()
    apilar(p,elem)

#Imprime la Pila original   
print ("Imprime los datos de la pila")
for i in range (0, tamanio(p)):
    elem=desapilar(p)
    apilar(paux,elem)
    print (elem)
    
#Ojo!! para imprimir la pila hay que ir recuperando los datos pero para probar
#Prueba no hacer, muestra que quedo la pila original vacia y la auxiliar con datos
print ("pila original y auxiliar")
print (p)
print (paux)

#pasamos los datos de la pila auxiliar a la original
copiarPila(p,paux)
print ("pila original y auxiliar despues del copiarpila")
#Prueba no hacer, muestra que quedo la pila original tiene los datos y la auxiliar esta vacia
print (p)
print (paux)

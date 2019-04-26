# Tad Cola

def crearCola():
    #Crea una cola vacia
    cola=[]
    return cola

def esVacia():
    #Retorna Verdadero si la cola no tiene elementos
    return len(cola)==0

def encolar(cola,elem):
    #Agrega un elemento al final de la cola
    cola.append(elem)
    
def desencolar(cola):
    #Retorna y elimina el primer elemento de la cola
    return cola.pop()

def tamanio(cola):
    return len(cola)

c=crearCola()
encolar(c,4)
encolar(c,'perro')
encolar(c,True)
#Imprime la Cola
print "Impresion de la cola"
print c  #solo para probar hay que ir recuperando cada elemento
#Imprime el tamanio de la cola
print "Impresion de la cantidad elementos de la cola"
print(tamanio(c))
encolar(c,7)
print c   #solo para probar hay que ir recuperando cada elemento

#Otra forma de definir esVacia 
#def esVacia():
#    if len(cola)==0:
#        return True
#   else:
#       return False

# Tad Pila

def crearPila():
    #Crea una pila vacia
    pila=[]
    return pila

def esVacia(pila):
    #Retorna Verdadero si la pila no tiene elementos
    return len(pila)==0

def apilar(pila,elem):
    #Agrega un elemento al final de la pila
    pila.append(elem)
    
def desapilar(pila):
    #Retorna y elimina el ultimo elemento de la pila
    elem=pila[len(pila)-1]
    pila.pop()
    return elem

def tamanio(pila):
    #Retorna la cantidad de elementos de la pila
    return len(pila)

def copiarPila(pila1,pila2):
    while not esVacia(pila2):
        elem=desapilar(pila2)
        apilar(pila1,elem)
        


#Otra forma de definir esVacia 
#def esVacia():
#    if len(pila)==0:
#        return True
#   else:
#       return False

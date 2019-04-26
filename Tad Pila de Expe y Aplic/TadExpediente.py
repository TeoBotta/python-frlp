# Tad Expediente

def crearExpe():
    #Crea un expediente vacio
    expediente=[0,""]
    return expediente

def cargarExpe(expediente,n,t):
    #Carga los datos de un expediente
    expediente[0]=n
    expediente[1]=t
    
def verNum(expediente):
    #Retorna el numero de un expediente
    return expediente[0]

def verTipo(expediente):
    #Retorna el tipo de un expediente
    return expediente[1]

def modiNum(expediente,n):
    #Modifica el numero de expediente
    expediente[0]=n

def modiTipo(expediente,t):
    #Modifica el tipo de un expediente
    expediente[1]=t

def asignarExpe(expediente1,expediente2):
    #Asigna los datos de un expediente en otro
    modiNum(expediente1,verNum(expediente2))
    modiTipo(expediente1,verTipo(expediente2))
    

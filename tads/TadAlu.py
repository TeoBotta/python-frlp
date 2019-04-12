# Tad Alu

# Se declara pass cuando necesitamos a la
# función sintátictamente pero no queremos
# que haga nada. Funciona como un null statement

# A diferencia de una línea de comentario que es
# ignorada completamente, el pass no es ignorado.

# Sirve por ejemplo si queremos tener una función 
# que queremos que esté en el código pero se quiere
# implementar más adelante. 


#Interface

def crearAlu():pass
    #Crea un alumno vacio

def cargarAlu(alumno,n,l,p):pass
    #Carga los datos de un alumno
	
def verNom(alumno):pass
    #Retorna el nombre de un alumno

def verLega(alumno):pass
    #Retorna el nombre de un alumno

def verProm(alumno):pass
    #Retorna el nombre de un alumno

def modiNom(alumno,n):pass
    #Modifica el nombre de un alumno

def modiLega(alumno,l):pass
    #Modifica el nombre de un alumno

def modiProm(alumno,p):pass
    #Modifica el nombre de un alumno

def asignarAlu(alumno1,alumno2):pass
    #Asigna los datos de un alumno en otro
	
	
#Implementacion
	
def crearAlu():
    #Crea un alumno vacio
    alumno=["",0,0]
    return alumno

def cargarAlu(alumno,n,l,p):
    #Carga los datos de un alumno
    alumno[0]=n
    alumno[1]=l
    alumno[2]=p

def verNom(alumno):
    #Retorna el nombre de un alumno
    return alumno[0]

def verLega(alumno):
    #Retorna el nombre de un alumno
    return alumno[1]

def verProm(alumno):
    #Retorna el nombre de un alumno
    return alumno[2]

def modiNom(alumno,n):
    #Modifica el nombre de un alumno
    alumno[0]=n

def modiLega(alumno,l):
    #Modifica el nombre de un alumno
    alumno[1]=l

def modiProm(alumno,p):
    #Modifica el nombre de un alumno
    alumno[2]=p

def asignarAlu(alumno1,alumno2):
    #Asigna los datos de un alumno en otro
    modiNom(alumno1,verNom(alumno2))
    modiLega(alumno1,verLega(alumno2))
    modiProm(alumno1,verProm(alumno2))


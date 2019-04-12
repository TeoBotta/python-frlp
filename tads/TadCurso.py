# Tad Curso

def crearCurso():
    #Crea un curso vacio
    curso=[]
    return curso

def agregarAlu(curso,a):
    #Agrega un alumno al curso
    curso.append(a)

def eliminarAlu(curso,a):
    #Elimina un alumno del curso
    curso.remove(a)

def recuperarAlu(curso,i):
    #Retorna el alumno de la posicion iesima
    return curso[i]

def tamanio(curso):
    #Retorna la cantidad de alumnos del curso
    return len(curso)
	
def existe(curso,a):
    #Retorna true o false si el alumno a pertenece o no al curso
	return a in curso



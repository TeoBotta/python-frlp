#ESPECIFICACIÓN

def crearSupermercado():pass
    #Crea un supermercado vacio, sin producto.

def agregarProducto(super,producto):pass
   #Agrega un producto al supermercado

def eliminarProducto(super,producto):pass
    #Elimina un producto del supermercado
 
def recuperarProducto(super,i):pass
    #Retorna el producto de la posicion iesima

def tamanio(superm):pass
    #Retorna la cantidd de productos del supermercado
	
def existe(super,producto):pass
    #Retorna true o false si el producto a pertenece o no al supermercado
	
#IMPLEMENTACIÓN

def crearSupermercado():
    #Crea un supermercado vacio, sin producto.
		super=[]
		return super

def agregarProducto(super,producto):
   #Agrega un producto al supermercado
   """super.insert(0,producto) #inserta al inicio
   super.insert(len(super),producto) #inserta al final, primero se fija cuantos productos tiene el super, y con eso saca a donde tiene que insertar.
   """
   super.append(producto) #inserta al final

def eliminarProducto(super,producto):
    #Elimina un producto del supermercado
	super.remove(producto)
 
def recuperarProducto(super,i):
    #Retorna el producto de la posicion iesima
	return super[i]

def tamanio(superm):
    #Retorna la cantidd de productos del supermercado
	return len(superm)
def existe(super,producto):
    #Retorna true o false si el producto a pertenece o no al supermercado
	return producto in super
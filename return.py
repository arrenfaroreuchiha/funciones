#problema con parametros y return
#parametros son las variables que pasamos por la funcion
def suma(a, b):
    total = a + b
    return total
#---------------------------------------------
def index(c):
    a = int(raw_input("Ingrese el valor A:"))
    b = int(raw_input("Ingrese el valor B:"))
    return suma(a, b) * c
#----------------------------------------------------

def write():
    c = 50
    return index(c)
#-------------------------------------------------
resul = write()#esto es lo primero que se ejecuta 
print "La suma es: ", resul
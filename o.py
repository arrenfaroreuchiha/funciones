# *-* coding: utf-8 *-*
print "uso del def"


def a():
	cantidad = int(raw_input("cuantos numeros:"))
	global condicional1, numeros
	condicional = 0
	condicional1 = 0
	condicional2 = 0
	numeros = 0
	return b(cantidad)

def b(cantidad):
	condicional = 0
	condicional1 = 0
	for i in range(cantidad):
		numero = int(raw_input("cual es el numero:"))
		condicional1 = condicional1 + numero
		condicional += 1
	lista = [condicional1, condicional]
	return lista
	

def c(lista):
	condicional = lista[1]
	condicional1 = lista[0]
	print "esta es la suma:", condicional1
	print "estos son la cantidad de numeros que pasaron", condicional
		
	

lista = a()
c(lista)


# -*- coding: utf-8 -*-
print "serie de fibonacci"

def entra():
	a = 1
	b = 0
	numero = int(raw_input("cual es el numero: "))
	return sale(a, b, numero)

def sale(a, b, numero):
	for i in range (0, numero):
		suma = b + a
		b = a
		a = suma
		print i
	lista = [suma] 
	return lista

def respuesta(lista):
	suma = lista[0]
	
	print "las suma es", suma

def mein():
	lista = entra()
	respuesta(lista)

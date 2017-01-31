# -*- coding: utf-8 -*-
print "multiplos de 3"

def entra():
	i = 1
	contador = 0
	numero = int(raw_input("cantidad de numeros:"))
	return calculo(i, contador, numero)
	

def calculo(i, contador, numero):
	for i in range (numero):
		numero2 = int(raw_input("numero:"))
		contador2 = numero2 % 3
		if contador2 == 0:
			print "es multiplo de 3"
			contador = contador + numero2
		else:
			print "no es multiplo de 3:", numero2
	lista = [contador]	
	return lista
	
	
	

def sale(lista):
	contador = lista[0]
	
	print "la suma de los multiplos de 3 es:", contador

def mein():
	lista = entra()
	sale(lista)



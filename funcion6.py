# -*- coding: utf-8 -*-
print "suma de numeros pares"

def entra():
	i = 1
	par = 0
	numero = int (raw_input("cantidad de numeros:"))
	return calcula(i, par, numero)

def calcula(i, par, numero):
	for i in range (numero):
		numero2 = int(raw_input("numero:"))
		contador = numero2
		contador = numero2 % 2
		if contador == 0:
			par = par + numero2
	lista = [par, numero]
	return lista

def sale(lista):
	par = lista[0]
	numero = lista[1]

	print "suma de numeros pares:", par
	print "el numero impar es:", numero

def mein():
	lista = entra()
	sale(lista)
# -*- coding: utf-8 -*-
print "mayor de numeros N"

def entra():
	contador = 0
	i = 1
	numero = int(raw_input("cantidad de numeros:"))
	return calcula(contador, i, numero)

def calcula(contador, i, numero):
	for i in range (numero):
		numero2 = int(raw_input("numero:"))
		if numero2 < numero2:
			numero2 = numero2
	lista = [numero2]
	return lista

def sale(lista):
	numero2 = lista[0]
	print "el numero mayor es:", numero2

def mein():
	lista = entra()
	sale(lista)
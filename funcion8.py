# -*- coding: utf-8 -*-
print "numero primo o no primo"

def entra():
	i = 1
	numero = int(raw_input("numero:"))
	calcula(i, numero)

def calcula(i, numero):
	for i in range (1):
		contador = numero % 2
		if contador == 1:
			print "el numero es primo"
		elif contador > 1:
			contador = numero % i 
		elif contador == 0:
			print "el numero no es primo"
	return
def mein():
	entra()
# -*- coding: utf-8 -*-

print "repaso de return"

def entra():
	cantidad = int(raw_input("cuantos numeros:"))
	return procesa(cantidad)

def procesa(cantidad):
	global vector
	vector = []
	print ("------------------------------------------")
	for i in range(cantidad):
		numero = int(raw_input("diguite el numero:"))
		vector.insert(i, numero)
		print "este es el vector", vector
	return 

	
	

entra()

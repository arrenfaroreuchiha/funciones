# -*- coding: utf-8 -*-
print "repaso de def"

vector = []
matriz = []



def entra():
	print "si en cuantos numeros elije 3 o 2, seran matrices si quiere un vector elije una cantidad diferente"
	cantidad = int(raw_input("cuantos numeros:"))
	return procesa(cantidad)

def procesa(cantidad):
	contando = 0
	contador = 0
	if cantidad == 2:
		for i in range(0, 2):
			matriz.append([])
			for j in range(0 , 2):
				numero = int(raw_input("cual es el numero:"))
				contando += 1
				contador = contador + numero
				matriz[i].append(numero)
		print "esta es su matris de dos por dos en fila", matriz
		print "este es el mayor de la matriz:", (max(max(matriz)))
		print "este es el menor de la matriz:", (min(min(matriz)))
		print "esta es la cantidad de numeros que hay en la matriz:", contando
		print "esto es una tupla", (tuple(matriz))
		print "---------------------------------------"
		print "esta es la matriz en orden"
		for i in range(0, 2):
			print matriz[i]
		print "la suma es:", contador
				
				
	elif cantidad == 3:
		#contador = 0
		for i in range(0, 3):
			matriz.append([])
			for j in range(0, 3):
				#contador = 0
				numero = int(raw_input("cual es el numero:"))
				contador = contador + numero
				matriz[i].append(numero)
		print "esta es su matris de tres por tres en fila", matriz
		print "este es el mayor de la matriz:", (max(max(matriz)))
		print "este es el menor de la matriz:", (min(min(matriz)))	
		print "esto es una tupla", (tuple(matriz))
		print ("-----------------------------------------")
		print "esta es la matriz en su orden"
		for i in range(0, 3):
			print matriz[i]
		print "esta es la suma", contador

	else:
		for i in range(cantidad):
			numero = int(raw_input("cual es el numero:"))
			vector.insert(i, numero)
		print "este es su vector:", vector
		print "esta es la cantidad de numeros que hay en el vector:", len(vector)
		print "este es el mayor de la matriz:", (max(vector))
		print "este es el menor de la matriz:", (min(vector))
		print "esto es una tupla:", (tuple(vector))
	
def mein():
	entra()

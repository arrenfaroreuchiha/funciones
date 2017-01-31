# *-* coding: utf-8-  *-*
print "uso de una matriz de 2x2 y 3x3"
matriz = []
lista = []
vector = []

cantidad = int(raw_input("2 o 3:"))
while cantidad != 2 and cantidad != 3:
	cantidad = int(raw_input("por favor marque 2 o 3:"))

if cantidad == 2:
	for i in range(0, cantidad):
		matriz.append([])
		for j in range(0, cantidad):
			numero = int(raw_input("cuales son los numeros:"))
			matriz[i].append(numero)
			matriz.sort()
	print "esta es la maytriz en fila", matriz
	print "------------------------------------"
	for i in range(0, 2):
		print  matriz[i]
	print "-------------------------------------"
	for i in range(0, cantidad):
		matriz[i]
		for j in range(0, cantidad):
			if i == j:
				lista.append(matriz[i][j])
	#print lista
	#print "--------------------------------------"
	f = 0
	for i in range(1, cantidad):
		r = lista[i] * lista[f]
	#print r
	#print "----------------------------------------"
	for i in range(0, cantidad):
		for j in range(0, cantidad):
			if i + j == cantidad - 1:
				vector.append(matriz[i][j])
	#print vector
	u = 0
	for i in range(1, cantidad):
		t = vector[i] * vector[u]
	#print t
	w = r - t
	print "esta es la determinante de la matriz de 2x2:", w

	
	
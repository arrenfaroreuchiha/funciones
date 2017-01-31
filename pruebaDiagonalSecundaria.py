matriz = []
diagonal = []
suma = 0

fila = []
fila2 = []
fila3 = []

def Diagonal():
	global suma
	global numeros
	numeros = int(raw_input("Cual es la Dimencion de la matriz: "))

	for i in range(0, numeros):
		matriz.append([])
		for j in range(0, numeros):
			numero = int(raw_input("Digita el numero [%d,%d] " % (i + 1, j + 1)))
			matriz[i].append(numero)

	# for j, item in enumerate(matriz):
	# 	print j, item
	print "\n"

	for i in range(0, numeros):
		for j in range(0, numeros):
			if i == 1:
				fila2.append(matriz[i][j]) 

			if i == 2:
				fila3.append(matriz[i][j]) 

	for i in range(0, numeros):
		for j in range(0, numeros):
			if i + j == numeros - 1:
				suma = suma + matriz[i][j]
				diagonal.append(matriz[i][j])

def MatrizCom():
	for i in xrange(0, numeros):
		print matriz[i]

def Fila():
	for i in xrange(0, numeros):
		for j in xrange(0, numeros):
			fila.append(matriz[i][j]) 
		break
	print "\n", fila

def Filas():
	for i in xrange(0, numeros):
		if i == 0:
			print "fila ", fila[i]
		elif i == 1:
			print "fila ", fila[i]
		if i > 0:
			print fila2[i]
			print fila3[i]

def Impresion():
	print "\nEsta es la diagonal secundaria: ", diagonal
	promedio = float(suma) / numeros**2
	print "\nEl promedio de la diagonal secundaria es: ", promedio 

def main():
	Diagonal()
	MatrizCom()
	Fila()
	Filas()
	Impresion()

def Suma():
	suma = 15 + 10
	return suma 
	
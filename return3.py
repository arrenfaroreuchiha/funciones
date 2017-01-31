# -*- coding: utf-8 -*-

def entra():
	print "calcular el exponentede N"
	i = 0
	potencia = 0
	base = int(raw_input("cual es la base:"))
	exponente = int(raw_input("cual es el exponente:"))
	return calculo(i, potencia, base, exponente)

def calculo(i, potencia, base, exponente):
	for i in range (1, exponente):
		if potencia == 0:
			potencia = base * base
		else:
			nuevapotencia = potencia * base
			potencia = nuevapotencia
	return potencia

potencia = entra()
print "la potencia es %d" % potencia
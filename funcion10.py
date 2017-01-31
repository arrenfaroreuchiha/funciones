# -*- coding: utf-8 -*-
import math
print "ecuacion cuadratica"

def entra():
	a = int(raw_input("numero 1:"))
	b = int(raw_input("numero 2:"))
	c = int(raw_input("numero 3:"))

	x = b ^ 2 - 4 * a * c
	return calcula(a, b, c, x)

def calcula(a, b, c, x):
	if a == 0:
		print "no se puede dividir"

	else:
		x = (-b) + math.sqrt (b) * (-4 * a * c) / 2 * a  
		x = (-b) - math.sqrt (b) * (-4 * a * c) / 2 * a
		if x > 0:
			print " es pisitiva"
		else:
		    print "es negativo"
	return

entra()

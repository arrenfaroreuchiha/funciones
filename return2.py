# -*- coding: utf-8 -*-
def variables():
	contador = 0
	total = 0
	calculo(contador, total)
	

def calculo(contador, total):
	while contador < 10:
		numero = int(raw_input("numero %d es:" % contador))
		total = total + numero 
		contador += 1
	print "el total es:", total
	print "cantidad de numeros inglesados:", contador
		
		
variables()




# -*- coding: utf-8 -*-
def jon():
	print "volumen del cilindro"
	r = int(raw_input("radio:"))
	h = int(raw_input("altura:"))
	return calculo(r, h)

def calculo(r, h):
	t = r ** 2
	v = t * h
	w = v * 3.14
	return w

res = jon()
#luego de haber guardado el valor en resul hacemos un print
print "el volumen es, ",  res

# -*- coding: utf-8 -*-
def entra():
	print "precios-promedio-iva-subtotal-total de un producto"
	global i, a, b, c, cantidad
	i = 1
	a = 1
	b = 2
	c = 3
	print "harina pan = $2500-1"
	print "aceite = $3000-2"
	print "bolsa de leche = $2300-3"
	cantidad = int(raw_input("cuantos productos:"))
	

def circula():
	global condicional, condicional1, condicional2, condicional3
	condicional = 0
	condicional1 = 0
	condicional2 = 0
	condicional3 = 0
	producto = 4
	for i in range (cantidad):
		while producto > 3:
			print "por favor marque el producto con su respectivo numero(1,2,3)"
			producto = int(raw_input("cual producto:"))
	if producto == 1:
		cantidad1 = int(raw_input("cantidad:"))
		global condicional
		condicional = 2500 * cantidad1
		producto = 4
		
	elif producto == 2:
		cantidad2 = int(raw_input("cantidad:"))
		global condicional1
		condicional1 = 3000 * cantidad2
		producto = 4
		
	elif producto == 3:
		cantidad3 = int(raw_input("cantidad"))
		global condicional2
		condicional2 = 2300 * cantidad3
		producto = 4
	lista = [condicional, condicional2, condicional3]
	return lista
		

def sale(lista):
	condicional = lista[0]
	condicional2 = lista[1]
	condicional3 = lista[2]

	subtotal = condicional + condicional2 + condicional3
	print "el subtotal es:", subtotal

	iva = subtotal * 16 / 100
	print "el iva es: %d" % iva

	total = subtotal + iva
	print "el total es: %d" % total
	return

def main():
	entra()
	lista = circula()
	sale(lista)
	
	




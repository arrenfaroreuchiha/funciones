# -*- coding: utf-8 -*-
print "promedio de materias y calificacion"
def entra():
	i = 0
	promedio = 1
	materias = int(raw_input("cuantas materias:"))
	condicional = 0
	condicional1 = 0
	return calculo(i, promedio, materias, condicional, condicional1)

def calculo(i, promedio, materias, condicional, condicional1):
	for i in range (materias):
		notas = float(raw_input("puntaje:"))
		condicional = notas + condicional
		creditos = float(raw_input("creditos"))
		condicional1 = creditos + condicional1
	lista = [condicional, condicional1, materias]
	return lista

def salida(lista):
	condicional = lista[0]
	condicional1 = lista[1]
	materias = lista[2]
		
	promedio = condicional / materias
	print "suma de notas finales:", condicional
	print "suma de creditos finales:", condicional1
	print "promedio del semestre:", promedio
	
lista = entra()
salida(lista)


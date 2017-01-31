# -*- coding: utf-8 -*-
print "promedio de materias y calificacion"
def entra():
	#i = 0
	promedio = 1
	materias = int(raw_input("cuantas materias:"))
	global condicional3, condicional1
	condicional3 = 0
	condicional1 = 0
	return circula(materias, promedio)

def circula(materias, promedio):
	for i in range(materias):
		notas = float(raw_input("puntaje:"))
		condicional3 = notas + condicional3
		creditos = float(raw_input("creditos"))
		condicional1 = condicional1 + creditos
	lista = [condicional3, condicional1]
	return lista

def sale(lista):
	condicional3 = lista[0]
	condicional1 = lista[1]
	promedio = condicional / materias
	print "suma de notas finales:", condicional3
	print "suma de creditos finales:", condicional1
	print "promedio del semestre:", promedio
	

lista = entra()
sale(lista)

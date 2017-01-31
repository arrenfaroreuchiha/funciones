# -*- coding: utf-8 -*-
print "promedio de materias y calificacion"
def entra():
	global i, promedio, materias, condicional, condicional1
	i = 0
	promedio = 1
	materias = int(raw_input("cuantas materias:"))
	condicional = 0
	condicional1 = 0


def circula():
	for i in range (materias):
		notas = float(raw_input("puntaje:"))
		global condicional
		condicional = notas + condicional
		
	
		creditos = float(raw_input("creditos"))
		global condicional1
		condicional1 = creditos + condicional1


		promedio = condicional / materias
		print "suma de notas finales:", condicional
		print "suma de creditos finales:", condicional1
		print "promedio del semestre:", promedio

def main():
	entra()
	circula()
	
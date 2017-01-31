
tupla = ("hola", "mundo")
lista = ["hola", "mundo"]
lista[0] = "Loca de eduardo"
print lista
dic = {"nombre": 'John', "edad": 22}
dic2 = {"clave": 'valor', "edad": 22}
#dic.clear() vaciar diccionario

print dic["nombre"]

keys = dic.keys()
print list(keys)

for clave, valor in dic.iteritems():
	print "EL diccionario con la clave %s y su valor es %s" % (clave, valor)

#----------------------------------------------------------------------------

secuencia = ["Nombre", "Edad", "Sexo"]
dic3 = dict.fromkeys(secuencia)
print dic3
dic3["Nombre"] = "John"
dic3["Edad"] = 22
dic3["Sexo"] = "M"
print dic3

#JSON
#dic4 = { {"Frutas": {"Nombre": "Pera"}, "Verduras": {"Nombre": "yuca"}} }

#print dic4
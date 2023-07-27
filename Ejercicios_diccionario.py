miDiccionario = {"Alemania":"Berlin","Francia":"París","Reino Unido":"Londres","España":"Madrid"}

#Como añadimos a un diccionario otro elemento
miDiccionario["Italia"]="Lisboa"

print(miDiccionario)

#Como actualizar un diccionario
miDiccionario["Italia"]="Roma"
print(miDiccionario)

#Como eliminar un elemento de un diccionario
del miDiccionario["Francia"]
print("---Eliminando Francia------")
print (miDiccionario)

otroDiccionario = {"Alemania":"Berlin",23:"Jordan","Mosqueteros":3}
print(otroDiccionario)


miTupla = ["España","Francia","Reino Unido","Alemania"]
#Asignando una tupla a un diccionario
miDiccionario2 = {miTupla[0]:"Madrid",miTupla[1]:"París",miTupla[2]:"Londres",miTupla[3]:"Berlin"}

print(miDiccionario2)

#Un diccionario dentro de un diccionario y dentro de ese diccionario se haya una tupla
miNuevoDiccionario = {23:"Jordan" , "Nombre":"Michael","Equipo":"Chicago","anillos":{"temporadas":[1991,1992,1993,1996,1997,1998]}}

print(miNuevoDiccionario)
#Claves del diccionario
print(miNuevoDiccionario.keys())
#Valores del diccionario
print(miNuevoDiccionario.values())

#Cantidad de valores del diccionario
print (len(miNuevoDiccionario))



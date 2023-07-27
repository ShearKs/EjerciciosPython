#Ejemplo de lista

miLista = ["Pepe","Juan","Teodoro","Juan Manuel",6,37]

#Mostramos el penultimo
print (miLista[-2])


#Mostramos solo 3 elementos
print (miLista[0:3])

#Python entiende que ya has puesto el 0 , y te muestra desde el 0 hasta el 3
print (miLista[:3])

print (miLista[1:3])

#Accedemos desde el que tiene indice 2 hasta el final
print (miLista[2:])

#Agregamos un elemento a la lista
miLista.append("Sergio")

#Mostramos otra vez la lista completa con el elemento que hemos añadido
print(miLista)

#Insertamos el número 100 en la posición 2
miLista.insert(2,100)

#Vemos como nos lo inserta
print(miLista[:])

#Agregamos más elementos
miLista.extend(["Real","De","Madrid"])

print(miLista[:])

#Si queremos saber el indice de un elemento
#Y como bien muestra es la posición 4
print(miLista.index("Juan Manuel"))

#Imprime true o false si ese elemento está en la lista
#Nos devuelve true ya que real si que está en nuestra Lista 
print("Real"   in miLista)

#La función remove elimina el elmento de la lista que tú le indiques
miLista.remove(100)
print(miLista)

miLista.remove("Sergio")
print(miLista)

#Elimina el último elemento de la lista
miLista.pop()
print(miLista[:])

miLista2 = ["Marta",2,"Manuel"]

#Unimos las dos listas

miResultadoL = miLista + miLista2

print(miResultadoL) 



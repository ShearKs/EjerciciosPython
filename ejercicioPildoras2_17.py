#Crea un programa que pida números positivos indifinidamente

num = int(input("Introduce un número positivo: "))

#Tupla donde guardaremos todos nuestros número positivos
listadoPares = []

#Suma de todos los números positivos introducidos por el usuario
sumaTotal = 0

while num > 0:
    listadoPares.append(num)
    num = int(input("Introduce otro número positivo: "))

for i in listadoPares:
    sumaTotal += i

print("Todos los numeros que has introducido: ",listadoPares)
print("Suma Total de los números ",sumaTotal)
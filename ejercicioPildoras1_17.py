# Crea un programa que pida números infinitamente.
# Los números introducidos deben ser cada vez mayores
# El programa finalizará cuando se introduce un número menor que el anterior.

#numeros que vamos a introducir que es lo que vamos a realizar con una tupla
numeros = []


num1 = int(input("Introduce un número: "))
numeros.append(num1)

num2 = int(input("Introduce otro número: "))


while num2 > num1:
    numeros.append(num2)

    #Hacemos que la variable num1 sea el ultimo
    num1 = num2
    num2 = int(input("Escriba otro número "))


print("Fin del programa ")
print("Números introducidos: ",numeros)




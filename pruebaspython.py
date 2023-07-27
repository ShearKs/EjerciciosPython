# -*- coding: utf-8 -*-
# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.


#Ejercicio1
'''
x = float(input("Ingresa el valor para x: "))

# coloca tu codigo aqui
y=(1/(x+1/(x+1/(x+1/x))))

print("y =", float(y))

print("valor : ",4%11)
'''

#Ejercicio 2
'''
ingreso=float(input("Ingrese el ingreso anual:"))


if(ingreso<85528):
    impuesto=(0.18*ingreso)-556.2
    if impuesto <0:
        impuesto=0.0
else:
    impuesto=14839.2+(0.32*(ingreso-85528))
    if impuesto <0:
        impuesto=0.0
  
'''
'''    
i = 0
while i <= 100:
    print("holi guapi",i)
    i += 1 


for i in range (101):
    print("holi soy un for",i)
    pass'''
''''
pow = 1
for i in range(16):
    print ("2 a la potencia del camnion", i, "es", pow)
    pow=pow*2'''
    
    
# break - ejemplo
'''
print("La instruccion de ruptura:")
for i in range(1,6):
    if i == 3:
        break
    print("Dentro del ciclo.", i)
print("Fuera del ciclo.")

# continua - ejemplo

print("\nLa instruccion continue:")
for i in range(1,6):
    if i == 3:
        continue
    print("Dentro del ciclo.", i)
print("Fuera del ciclo.")'''

'''
palabra=input("ingresa un palabra")

while True:
    if (palabra=="chupacabra"):
        print("Has dejado el ciclo con exito")
        break'''

    
#COMEDOR DE PALABRAS
# Indicar al usuario que ingrese una palabra
# y asignarlo a la variable userWord.
'''
palabraSinVocal = ""
userWord=raw_input("ingresa una palabra  :  ")
userWord=userWord.upper()

for letra in userWord:
    # Completa el cuerpo del ciclo for.
    if (letra=="A"):
        continue
    elif (letra=="E"):
        continue
    elif (letra=="I"):
        continue
    elif (letra=="O"):
        continue
    elif (letra=="U"):
        continue
    letra=palabraSinVocal
    print("\n"+palabraSinVocal)
    '''
 
'''   
bloques = int(input("Introduzca el numero de bloques disponibles: "))

utilizados = 0
altura = 0
por_fila = 1
 
while True:
    utilizados += por_fila
    if utilizados > bloques:
        break
 
    altura += 1
    por_fila += 1
 
 
print("La altura de la piramide es de: ", altura) '''   

'''
for i in range(1, 10):
    if i % 2 == 0:
        print(i)'''  

'''
for i in range(1,11):
    if (i%2!=0):
        print(i)    '''   
'''
x = 1
while x < 11:
    if(x%2!=0):
        print(x)
    x=x+1 '''
'''
n=3

while n>0:
     print(n+1) 
     n-=1
     print("el valor actual de n es : ",n)
else:
     print(n)
     
     
     
for i in range[0, 6, 3]:
    print(i)  '''
    
'''
    
beatles=[]
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")



for i in beatles:
    if len(beatles) <=4:
        i=input("Introduce los siguientes  miembros de la banda : ")
        beatles.append(i)
    
print("Has introducido a los beatles que faltaban" ,beatles)


#Eliminamos a los que acabamos de anadir
del beatles[-2],beatles[-1]

print("Ya estan elimniandos",beatles)

#insertamos a Ringo Starr

beatles.insert(0,"Ringo Starr")

#Los Beatles se quedan asi
print("La lista se ha quedado de la siguiente manera",beatles)

# probando la longitud de la lista
print("Los Fab", len(beatles)) '''

'''
miLista = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
nuevaLista=[]

for i in miLista:
    if i in miLista:
        del miLista[i]
        nuevaLista=miLista[:]
        
print("La lista solo con elementos unicos:")
nuevaLista.sort()
print(nuevaLista) '''


def evenNumLst(ran):
    lst = []
    for num in range(ran):
        #El 0 se considera como par
        if num % 2 == 0:
            lst.append(num)
    return lst

print(evenNumLst(11))


def listUpdater(lst):
    updList = []
    for elem in lst:
        elem **= 2
        updList.append(elem)
    return updList

l = [1, 2, 3, 4, 7]
print(listUpdater(l))


def sum(x):
    var = 7
    return x + var

print(sum(4))    # salida: 11

def factorialFun(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    
    producto = 1
    for i in range(2, n + 1):
        producto *= i
    return producto

print(factorialFun(5))



grupo = {}

while True:
    nombre = input("Ingresa el nombre del estudiante (o exit para detenerse): ")
    if nombre == 'exit':
        break
    
    calif = int(input("Ingresa la calificacin del alumno (0-10): "))
    
    if nombre in grupo:
        grupo[nombre] += (calif,)
    else:
        grupo[nombre] = (calif,)
        
for nombre in sorted(grupo.keys()):
    sum = 0
    contador = 0
    for calif in grupo[nombre]:
        sum += calif
        contador += 1
    print(nombre, ":", sum / contador)
    
    
    
polEspDict = {
    "zamek" : "castillo",
    "woda"  : "agua",
    "gleba" : "tierra"
    }

for item in polEspDict.items():
    print(item)
    
    
polEspDict = {
    "zamek" : "castillo",
    "woda"  : "agua",
    "gleba" : "tierra"
    }

if "zamek" in polEspDict:
    print("SI")
else:
    print("NO")
    
    
polEspDict = {
    "zamek" : "castillo",
    "woda"  : "agua",
    "gleba" : "tierra"
    }

polEspDict = {
    "zamek" : "castillo",
    "woda"  : "agua",
    "gleba" : "tierra"
    }


lst = [1, 2, 3, 4, 5]
lst2 = []
agregar = 0

#Clave para entender el bucle for
for number in lst:
    agregar += number
    lst2.append (agregar)

print(lst2)

def f(x):
    if x==0:
        return 0
    return x+f(x-1)

print(f(3))


from platform import platform

print(platform())
print(platform(1))
print(platform(0, 1))



from platform import system

print("El sistema es :"+system())

from platform import version

print(version())


from platform import python_implementation, python_version_tuple

print(python_implementation())

for atr in python_version_tuple():
    print(atr)
    
    
# Rodajas o rebanadas

alpha = "abdefg"

print(alpha[1:3])
print(alpha[3:])
print(alpha[:3])
print(alpha[3:-2])
print(alpha[-3:4])
print(alpha[::2])
print(alpha[1::2])

print('[' + 'gamma'.center(20, '*') + ']')

print("[" + "             tau ".lstrip() + "]")
print("www.cisco.com".lstrip("w."))
print("pythoninstitute.org".lstrip(".org"))


print("www.netacad.com".replace("netacad.com", "pythoninstitute.org"))
print("This is it!".replace("is", "are"))
print("Apple juice".replace("juice", ""))


# igual que el find() pero comienzan desde el final
print("tau tau tau".rfind("ta"))
print("tau tau tau".rfind("ta", 9))
print("tau tau tau".rfind("ta", 3, 9))

#Divide la cadena y crea una lista de todas las subcadenas detectadas
print("phi       chi\npsi".split())

#Quita todos los espacios tanto de delante como de detras
print("[" + "   aleph   ".strip() + "]")

# Intercambia las letras mayusculas y minusculas
print("Yo se que no se nada.".swapcase())

print()

# Pone cada palabra a mayusculas
print("Yo se que no se nada. Parte 1.".title())

print()

# Cambia todas las minusculas por mayusculas
print("Yo se que no se nada. Parte 2.".upper())

#Comparacion
print('beta' > 'Beta')

# Demostracion de la función sorted()
firstGreek = ['omega', 'alfa', 'pi', 'gama']
firstGreek2 = sorted(firstGreek)

print(firstGreek)
print(firstGreek2)

firstGreek = ['omega', 'alfa', 'pi', 'gama']
firstGreek2 = sorted(firstGreek)

print(firstGreek)
print(firstGreek2)

print()


secondGreek = ['omega', 'alfa', 'pi', 'gama']
print(secondGreek)

secondGreek.sort()
print(secondGreek)

print('Mike'>'mike')


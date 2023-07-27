def mensaje():

	print ("Mi primera función")


mensaje()


def suma():
	num1 = 2
	num2 = 3
	suma = num1 + num2
	#muestra la suma de num1 y num2
	print ("La suma es ",suma)

suma()	


#Suma con parámetros

num1 = 5

num2 = 10

def suma_para(num1,num2):
	print ("La suma de la función con parametros es ",
		num1+num2)

suma_para(num1,num2)

##Dada dos numero atribuidos por el usuario
suma_para(10,10)

#Vamos a asignar un valor a una función

def suma_retorno(num1,num2):
	resultado = num1 + num2
	return resultado

#Almacenamos en esta variable el retorno que nos ha dado la función
almacena_resultado = suma_retorno(5,6)

#Visualizamos la variable donde hemos guardado el resultado
print (almacena_resultado)

#Lamdba es una manera de crear funcion de manera rapida
#f=lambda argumento:resultado
#The Keyword lambda le ofrece al programador una alternativa de sintaxis
#para la creacion de una funcion

def function_1(x):return x**2 #el return podria estar abajo, esto es otra forma de escruibirlo
def function_2(x):return x**3 
def function_3(x):return x**4

callbacks = [function_1, function_2, function_3] #Crea una lista de funciones

print('\nNamed Functions:')
for function in callbacks:print('Result:',function(3))

#---------La segunda manera de hacer esto con Lambda----#

callbacks=\ #El caracter \ permite escribir el codigo en la proxima linea
[lambda x : x**2, lambda x : x**3, lambda x : x**4]
print('\nAnonymous Functions:')
for function in callbacks : print('Result:', function(3)) #Requiere menos lineas de codigo

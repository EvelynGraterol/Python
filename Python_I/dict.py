#En otros lenguajes de programacion una lista es llamada "array o arreglo" y un diccionario es llamado un "associative array"
#que seria un arreglo asociativo o una lista asociativa veamos.
#La Data es frecuentemente asociada a una llave:valores pares.Por ejemplo cuando
#tu llenas un formulario en la web, tipeas un valor de texto como campo input
#esta tipicamente sociado con un nombre de campo al texto llamado llave

dict = {'name':'Bob','ref':'Python','sys':'Win'}
print('Dictionary:',dict)
print('\nReference:',dict['ref'])
print('\nKeys:',dict.keys()) #Las llaves que abren al valor que esta adentro

del dict['name'] #borra un par del diccionario 
dict['user'] = 'Tom' # anade un par
print('\nDictionary:',dict)

print('\nIs There A name Key?:','name' in dict)#el in me dice con verdadero o falso, si esa llave existe dentro de diccionario

                          

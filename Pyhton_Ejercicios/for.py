#Con la funcion range(que inicia en 0) yo puedo establecer el inicio, el final
#y el step

chars = ['A','B','C'] #Lista
fruit = ('Apple','Banana','Cherry')#Tupla(No pueden ser manipulados sus datos)
dict = {'name':'Mike','ref':'Python','sys':'Win'} #dictionary

print('\nElements:\t',end='') #Importantsimo la identacion,porque de ella depende el orden del codigo
for item in chars:
    print(item, end='')

print('\nEnumerated:\t',end='')
for item in enumerate(chars): # La funcion enumerate me da indice de la posicion del item
    print(item,end='')

print('\nZipped:t', end = '')
for item in zip(chars, fruit):#La funcion me da el conjunto para cada elemnto
    print(item, end='')

print('nPaired:')
for key, value in dict.items(): #da como output la llave y su respuesta
        print(key, '=',value)

#En programacion en Python cualquier cosa que contiene multiples items puede
#ser looped o considerado como "iterable".         
        

    

    

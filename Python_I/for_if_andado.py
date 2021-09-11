#Uso del for con un if anidado

list1 = [1,2,3,4,5]
for item in list1:
    if item == 3:
        print('El valor se encuentra en la la lista')
        break #Que rompa el ciclo una vez que lo encuentre
else:
    print('El valor no se encuentra en la lista')
        

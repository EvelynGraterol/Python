basket = ['Apple','Bun','Cola']
crate = ['Egg','Fig','Grape']

print('Basket List:',basket)
print('Basket Elements:',len(basket))

basket.append('Dawson')  #nombro la lista.comando para agrgar eultimo.elnuevo item
print('Appended:',basket)
print('Last Item Removed:',basket.pop())#Remueve el uultimo item agregado
print('Basket List:',basket)


basket.extend(crate)#Coloca una lista detro de la otra
print('Extend:',basket)

del basket[1] #Elimina el elemento 1 de la lista basket
print('Item Removed:',basket)

del basket[1:3] #Remueve los elementos de la posicion de 1 al 3 de la lista grande de basket
print('Slice Removed:',basket)

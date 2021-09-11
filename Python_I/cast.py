
#Transformacion de numeros 
a = input('Enter a Number:')
b = input('Now  enter Another Number')

sum = a + b #para que la sea una suma verdadera, la asignacion debe ser numerica
print('\nData Type sum:',sum,type(sum))

sum = int(a)+int(b) #Al cambiarlo a interger realiza la suma
sum=float(sum)
print('Data Type sum:', sum, type(sum))

sum=chr(int(sum)) # La letra que se obtiene aqui depende del valor asignado en ASCII
print('Data Type sum:',sum,type(sum))


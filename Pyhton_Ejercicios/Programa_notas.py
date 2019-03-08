#Desarrollar un programa que permita la carga de 10 valores por teclado
#y nos muestre posteriormente la suma de los valores ingresados y su promedio.

suma=0
for f in range(10):
    valor=int(input("Ingrese valor:"))
    suma=suma+valor
print("La suma es") #Observe la importancia que tiene la indexacion del print
print(suma)         #si queremos que la suma y el promedio sea general
promedio=suma/10    #Debe estar alineado con el for.
print("El promedio es:") #Prueba tu mismo moviendo este bloque de codigo
print(promedio)          #a la altura de la suma y observa como se calcula para
                         #cada valor.

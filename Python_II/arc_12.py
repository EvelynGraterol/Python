#En python no se usa switch por su simplicidad, se utiliza operadores de comparación concatenadados,
# que  nos permite evaluar muchas condiciones encadenadas.

#Una alternativa puede ser el uso de diccionarios cuando hay que evaluar varias condiciones 
#como python fuertemente tipado no concatena diferente tipos de datos 17.35
#al fallar en la primera pareja(condicion) automaticamente ignora todo lo demás y pasa al else.
#las condiciones se deben cumplir de izq a derecha
#Supongamos que quiero comparar el salario de varios empleados

salario_presidente = int(input("Introduce el salario del presidente: "))
print("Salario  presidente: " + str(salario_presidente))

salario_director = int(input ("Introduce el salario del director: "))
print("Salario director: " + str(salario_director))

salario_jefe_area = int(input("Introduce el salario del jefe de area: "))
print("Salario jefe de area: " + str(salario_jefe_area))

salario_administrativo = int(input("Introduce el salario administrativo: "))
print("Salario administrativo: " + str(salario_administrativo))

if salario_administrativo < salario_jefe_area < salario_director < salario_presidente:
    print("Todo funciona correctamente")

else:
    print("Algo falla en esta empresa")

#prueba datos correctos 3500, 3500, 2500, 2500, 2000, 2000
#prueba de falla 4000, 3000, 3150, 1000
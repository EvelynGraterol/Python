#cuantos and y or se pueden concatenar? se pueden concatenar todos lo que quieran 1250
#or : o sino
#and : y si 

print("Programa de becas")

distancia_escuela = int(input("Introduce la distancia a la escuela en km "))
print(distancia_escuela)

numero_hermanos=int(input("Introduce el numero de hermanos en el centro"))
print(numero_hermanos)

salario_familiar=int(input("Introduce salario anual bruto "))
print(salario_familiar)

if distancia_escuela>40 and numero_hermanos>2 or salario_familiar<=20000: #con el or se le da mas peso al salario
    print("Tienes derecho a una beca")

else:
    print("No tienes derecho a beca")


""" Parte II de (13) funciones """

#Escoger una materia optativa desde un listado, 

print("Asignaturas optativas")
print("Asignaturas optativas: Informatica grafica - Pruebas de software - Usuabilidad y accesibilidad")
opcion = input("EScribe la asignatura escogida: ")

asignatura = opcion.lower()
if asignatura in ("informatica grafica", "pruebas de software", "usabilidad y accesibilidad"):

    print("Asignatura elegida " + asignatura)

else: 
    print("La asignatura no esta contemplada")



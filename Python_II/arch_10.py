
""" Parte I de (10) funciones """
#los  condicionales toman por defecto true
#las funciones permiten arrancar con un valor incial

def  evaluacion(nota):
    valoracion = "aprobado"  #con esta inicialización no hace falta hacer un else
    if nota<5:
        valoracion="suspendido"
    return valoracion

print(evaluacion(4))
print(evaluacion(6))


""" Parte II de (10) funciones """
#uso del imput()

print("Programación de evaluación de notas")

nota_alumno=input()                  #usuario introduce la nota por teclado

def  evaluacion2(nota):
    valoracion = "aprobado"          #con esta inicialización no hace falta hacer un else
    if nota<5:
        valoracion="suspendido"
    return valoracion

print(evaluacion2(int(nota_alumno))) #se debe convertir la nota a int

""" Parte III de (10) funciones """

print("Programación de evaluación de notas3")

nota_alumno3=input("Introduce la nota del alumno: ")                  #usuario introduce la nota por teclado

def  evaluacion3(nota):
    valoracion = "aprobado"          #con esta inicialización no hace falta hacer un else
    if nota<5:                       #la variable depende de su ambito
        valoracion="suspendido"
    return valoracion

print(evaluacion3(int(nota_alumno3))) #se debe convertir la nota a int


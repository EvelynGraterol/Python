
""" Parte I de (11) funciones """
# el else trabaja inmediatamente con el else que tiene mas arriba
#cuando tenemos elif, el else acompaña de toda la estructura

print("Verificación de acceso")

nota_alumno = int(input("Introduce tu nota, por favor: "))

if nota_alumno < 5:
    print("Insuficiente")

elif nota_alumno < 6:
    print("Suficiente")

elif nota_alumno<7:
    print("Bien")

elif nota_alumno<9:
    print("Notable")

else:
    print("Sobresaliente")
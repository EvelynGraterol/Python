#la función de tipo f, es una función especial
#en python la función tipo f nos permite jugar con formatos de forma diferente
#las llaves lo que hace es concatenar el texto con el valor de la variable

"""PARTE I"""

for i in range(5):
    print(f"valor de la variable {i}")

print('------')

for i in range(5):
    print("valor de la variable " + str(i))

print('------')

for i in range(5,50,3):
    print(f"valor de la variable {i}")


"""PARTE II"""
valido = False

email = input("Introduce tu email: ")

for i in range(len(email)):
    
    if email[i] == "@":
        valido = True

if valido:

    print("Email correcto")

else:

    print("Email incorrecto")

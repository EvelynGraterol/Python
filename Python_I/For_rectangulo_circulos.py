#Escribe un programa que pida el ancho y el elto de un  rectangulo
#y lo dibuje con el caracter'o'

ancho = int(input("Ingrese el ancho del rectangulo:" ))
alto = int(input("Ingrese el alto de; rectangulo: "))

for i in range(alto):
    for i in range(ancho):
        print('o', end="")
    print()
                  

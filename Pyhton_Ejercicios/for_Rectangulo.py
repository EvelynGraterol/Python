#Escribe un programa que pida el ancho y el alto de un rectangulo
#y lo dibuje con el caracter del producto

ancho = int(input("Ingrese el ancho del rectangulo: "))
alto = int(input("Ingrese el alto del rectangulo: "))

for i in  range(alto):
    for i in range(ancho):
        print('*',end="")
    print()
    




print("Bienvenido a la nueva Pizzeria")
x = int(input("Ingrese no mas de 5 ingredientes: "))
              

while x<5 :
    print("Indique los sabores de su preferencia")
    p = input('Agregar pina: ')
    pep = input('Agregar peperoni : ')
    jam = input('Agregar mozzarella: ')
    cho = input('Agregar choclo: ')
    ceb = input('Agregar cebolla: ')

    p = True
    if p :
       p = 100
       print(p) 

print("La cantidad de ingredientes proporcionada excede el numero permitido")

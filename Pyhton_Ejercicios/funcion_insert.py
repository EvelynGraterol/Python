numbers_list = [1,2,3,4,5]

def insert_numbers(numbers_list):
    numbers_list.insert(3,13)#El primer item corresponde a la posicion
                             #El segundo el numero a insertar
    print('la lista es:',numbers_list)
    return

insert_numbers(numbers_list) #Se hace un llamado a la funcion
                            #Para obtener el resultado

#Define un una funcion en la cual se repitan los valores
#que se encuentra en ella

def mi_funcion(cad,v=3,*todo): # (cadena,numeroderepeticiones,todosloselementos)
    print(cad*v)               #Primer elemento
    for cadena in todo:        #Aplicacion a todos los elementos
        print (cadena*v)

mi_funcion('Todo',1,'lo','que','vale','requiere','esfuerzo')#1 corresponde
#al numero de repeticiones dentro de la funcion

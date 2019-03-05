d = {'user':'bozo' , 'pswd':1234}
#d['user']
#d['pswd']

#Vamos a cambiar el usuario y agregar un id asociado

e = {'user2':'maria','pswd2':1456}
e['user2'] = 'luisa'
e['id']='45'


#Si se quiere eliminar un elemento conjunto de un diccionario se utiliza la
#palabra clave (del)

f = {'user3':'pedro','pswd3':7892,'id':55}
del f['user3'] #Remover un elemento par
f.clear()      #Remueve todos los elementos

#Obtener los valores de un diccionario de diferentes formas

dic = {'user4':'paula', 'pswd4':8757,'id4':33}
dic.keys #Lista de llaves
dic.values() #Lista de valores
dic.items() #Lista de item en forma de tuplas
    

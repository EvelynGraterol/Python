#Supplying argumennts#Puedo refinir argumentos arriba y abajo

def echo(user,lang,sys):
    print('User:',user,'Language:',lang,'Platform:',sys)
#echo('Mike','Python','Windows')
echo(lang='Python',sys='Mac OS',user='Anne')

def mirror(user='Carole',lang='Python'):
    print('\nUser:',user,'Language:',lang)

mirror()     #Cada uno de estos codigos me redefine la variable de acuerdo a como yo las quiera.
mirror(lang='Java') #Estos en basicamente es en matematica un cambio de variable como en las integrales
mirror(user='Tony') #Incluso al mandar a correr todos los casos, no existe interferencias de variables, porque estan contenidas dentro de un funcion
mirror('Susan','C++')

    

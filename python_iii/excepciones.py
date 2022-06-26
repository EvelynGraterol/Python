# PS C:\Users\Evelyn Graterol\Documents\practicas_deliberadas\practica_1> git clone https://github.com/EvelynGraterol/Python.git

##############################
###########PRD_1##############
##############################

def division(x, y):

    try:        
        return x/y

    except ZeroDivisionError:

        print('Error al intentar dividir entre cero')


def imprime_resultado( x, y):

    resultado = division(x, y)
    print ("La division de {} entre {} es {}".format(x, y, resultado))


#imprime_resultado(20,0)
imprime_resultado(50,2)




import pdb

pdb.set_trace()

def division(x,y):
    return x/y

def imprime_resultado(x, y):
    resultado = division(x,y)
    print("la division de {} con {} reporta {}".format(x,y,resultado))

imprime_resultado(20, 0)
#Ecuacion lineal
#importamos los modulos necesarios
import math
import numpy as np
from matplotlib import pyplot as plt

#Generamos los datos para el grafico
def f(x):
    return (x**2)

#Generamos los limite
x = np.linspace(-20, 20, num=100) #num-numero de muestras

#Creamos el grafico
plt.ion()
plt.plot(x, f(x), label="funcion f(x)")

#Colocamos las etiquetas de los ejes
plt.xlabel("Eje $x$")
plt.ylabel("Eje $f(x)$")

#Colocamos la leyenda
plt.legend()

#Colocamos el titulo del grafico
plt.title("Funcion de $f(x)$")

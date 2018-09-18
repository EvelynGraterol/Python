#Funcion Cubica
#Importamos todos los modulos necesarios
import math
import numpy as np
from matplotlib import pyplot as plt

#Generamos los datos para el grafico
def f(x):
    return (x)**3

#Generamos un segundo conjunto de datos para el grafico
x = np.linspace(-10, 10, num=25)

#Creamos el grafico
plt.ion()
plt.plot(x, f(x), label="funcion cubica")

#Colocamos las etiquetas de los ejes
plt.xlbel("Eje $x$")
plt.ylabel("Eje $y$")

#Colocamos la leyenda
plt.legend()

#Colocamos el titulo del grafico
plt.title ("funcion cubica")

#Ecuacion lineal
#importamos los modulos necesarios
import math
import numpy as np
from matplotlib import pyplot as plt

#Generamos los datos para el grafico
def f(x):
    return (3*x)+2 #Para funciones lineales no se usa np

#Generamos un segundo conjunto de datos para el grafico
x = np.linspace(-10, 2, num=10)

#Creamos el grafico
plt.ion()
plt.plot(x, f(x), label="funcion f(x)")

#Colocamos las etiquetas de los ejes
plt.xlabel("Eje $x$")
plt.ylabel("Eje $f(x)$")

#Colocamos la leyenda
plt.legend()

#Colocamos el titulo del grafico
plt.title("Funcion $f(x)$")

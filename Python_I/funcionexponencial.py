#Ecuacion exponencial
# Importamos los módulos necesarios
import math
import numpy as np
from matplotlib import pyplot as plt

# Generamos los datos para el gráfico
def  f(x):
    return np.exp(-x**2)
# Generamos un segundo conjunto de datos para el gráfico
x = np.linspace(-1, 5, num=30)

# Creamos el gráfico
plt.ion()
plt.plot(x, f(x), label="funcion f(x)")

#Colocamos las etiquetas de los ejes
plt.xlabel("Eje $x$")
plt.ylabel("Eje $f(x)$") #El simbolo dolar hace que salga en cursiva la letra

#Colocamos la leyenda
plt.legend()

#Colocamos el título del gráfico
plt.title("Funcion $f(x)$")


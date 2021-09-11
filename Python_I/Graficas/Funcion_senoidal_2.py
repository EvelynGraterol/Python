#Ejercicio graficando la funcion sen(x)
#Parte 2: Usando la libreria Math

import math
import matplotlib.pyplot as plt
import numpy as np


#Generamos  el conjunto de datos para el grafico

x = np.array(range(100))*0.1
y = np.zeros(len(x))
for i in range(len(x)):
    y[i]= 2*math.sin(4*x[i])-x[i]**2+10*x[i] #Hay que construir un arreglo vacion, para que luego ingresen cada valor de la funcion calculada.

#Creamos el grafico
plt.ion()
plt.plot(x,y)
         
#Colocamos etiquetas a los ejes
plt.xlabel("Eje $x$")
plt.ylabel("Eje $y$")

#Colocamos el titulo del grafico
plt.title("Funcion senoidal, segunda forma")

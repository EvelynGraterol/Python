#Ejercicio graficando la funcion sen(x)
#Parte 1:Usando la libreria numpy.Sin embargo, me gusta importar ambas
#librerias siempre al mismo tiempo,pero en este caso lo haré por separado

import numpy as np
import matplotlib.pyplot as plt

#Generamos los datos para el grafico (Definir la funcion)
def f(x):
    return 2*np.sin(4*x)-x**2+10*x #Importante:despues del np no debe existir ningun numero entero

#Generamos un segundo conjunto de datos para el grafico
x = np.arange(0,10,0.1) #Importante:Observar que arrange es usado con np

#Creamos el grafico, tambien puedes usar la funcion plt.show(), pero el codigo sigue corriendo.
plt.ion()
plt.plot(x, f(x))

#Colocamos las estiquetas de los ejes
plt.xlabel("Eje $x$")
plt.ylabel("Eje $y$")

#Colocamos el titulo del grafico
plt.title ("Funcion sinoidal")

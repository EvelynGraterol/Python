#Importar los modulos necesarios

import math
import numpy as np
from matplotlib import pyplot as plt

#Generamos los datos para el grafico
x = np.array(range(20))*0.1
y = np.zeros(len(x))
for i in range(len(x)):
    y[1] = math.sin(x[1])

#Creamos el grafico

plt.plot(x,y)
plt.show()

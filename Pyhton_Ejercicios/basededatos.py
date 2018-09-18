import pandas as pd
import math
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns

datos = pd.read_csv('movies2.csv')
df = pd.DataFrame(datos)

df.groupby('genres')['movie_facebook_likes'].sum().plot(kind='bar')

plt.show()

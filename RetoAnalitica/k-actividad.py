#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
import sklearn
from sklearn.cluster import KMeans
from sklearn.metrics import pairwise_distances_argmin_min
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.preprocessing import scale
import sklearn.metrics as sm
from sklearn import datasets
get_ipython().run_line_magic('matplotlib', 'inline')
from mpl_toolkits.mplot3d import Axes3D
plt.rcParams['figure.figsize'] = (16, 9)
plt.style.use('ggplot')


# In[78]:


dataframe = pd.read_csv(r"Videojuegos.csv") #Base de datos
dataframe.head()


# In[67]:


print(dataframe.groupby('Plati').size())


# In[24]:


dataframe.drop(['Platform'],1).hist()
plt.show()


# In[68]:


X = np.array(dataframe[["NA_Sales","EU_Sales","JP_Sales"]])
y = np.array(dataframe['Plati'])
X.shape


# In[83]:


colores=['blue','red','green','blue','cyan','yellow','orange','black','pink','brown','purple']
#NOTA: asignamos la posición cero del array repetida pues las categorias comienzan en i
asignar=[]
for row in y:
    asignar.append(colores[row])


# In[81]:


fig = plt.figure()
ax = Axes3D(fig)
colores=['blue','red','green','blue','cyan','yellow','orange','black','pink','brown','purple']
#NOTA: asignamos la posición cero del array repetida pues las categorias comienzan en i
asignar=[]
for row in y:
    asignar.append(colores[row])
ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=asignar,s=10);


# In[72]:


Nc = range(1, 20)
kmeans = [KMeans(n_clusters=i) for i in Nc]
kmeans
score = [kmeans[i].fit(X).score(X) for i in range(len(kmeans))]
score
plt.plot(Nc,score)
plt.xlabel('Number of Clusters')
plt.ylabel('Score')
plt.title('Elbow Curve')
plt.show()


# In[71]:


kmeans = KMeans(n_clusters=5).fit(X)
centroids = kmeans.cluster_centers_
print(centroids)


# In[33]:


# Obtenemos las etiquetas de cada punto de nuestros datos
labels = kmeans.predict(X)
# Obtenemos los centroids
C = kmeans.cluster_centers_
colores=['red','green','blue','cyan','yellow']
asignar=[]
for row in labels:
    asignar.append(colores[row])
fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=asignar,s=60)
ax.scatter(C[:, 0], C[:, 1], C[:, 2], marker='*', c=colores, s=1000);


# In[36]:


f1 = dataframe['NA_Sales'].values
f2 = dataframe['JP_Sales'].values
plt.scatter(f1, f2, c=asignar, s=70)
plt.scatter(C[:, 0], C[:, 1], marker='*', c=colores, s=1000)
plt.show()


# In[99]:


print (classification_report(y, labels));


# 
# ¿Crees que estos centros puedan ser representativos de los datos? ¿Por qué?
# 
# Si los representan debido a la relacion que tienen entre ellos, aunque si existe una rango amplio entre estos mismos datos, observando la gráfica notamos que su distribución es más densa en la parte inferior izquierda.
# 
# ¿Cómo obtuviste el valor de k a usar?
# 
# El número de cluster identificados por el algoritmo, es representado por k, es un método que se usa para identificar el número de cluster necesarios para el análisis de datos, usamos diferentes funciones, entre ellas el ciclo for, con cierto rango y al final graficamos los resultados.
# 
# ¿Los centros serían más representativos si usaras un valor más alto? ¿Más bajo?
# 
# Los centros tendrían más relevancia si se usara un valor más bajo, debido a la distribución de nuestros datos, en razón de que su aproximación a cero es mayor porque se calcula en escala de millones.
# 
# ¿Qué distancia tienen los centros entre sí? ¿Hay alguno que este muy cercano a otros?
# 
# La distancia se encuentra entre el renago de: 0.00-0.15, demostrando que la distancia entre los centros es pequeña porque la comparación de distancia se realiza entre regiones, no obstante si la comparación fuera global la distancia seria mayor.
# 
# ¿Qué pasaría con los centros si tuviéramos muchos outliers en el análisis de cajas y bigotes?
# 
# Tendria una variación amplia entre distancias existentes sobre los datos, en el análisis de cajas y bigotes los datos no estaría dentro de la región de las cajas, sino fuera de ellas.
# 
# ¿Qué puedes decir de los datos basándose en los centros?
# 
# Que se puede encontrar una relación entre las ventas por regiones y la cantidad de titulos que existen por consola.

# In[ ]:





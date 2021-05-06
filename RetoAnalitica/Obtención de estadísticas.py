#!/usr/bin/env python
# coding: utf-8

# # Ejercicio PANDAS

# Andrea González Arredondo A01351820
# Xavier Alfonso Barrera Ruiz A01702869  
# Olivia Araceli Morales Quezada A01707371
# José Pablo Cabos Austria A01274631
# RETO 6

# 1.-En este primer pequeño programa podemos observar como al principio importamosciertas librerías para que pueda funcionar,
# después le asignamos ciertos vectores a las variables, y con ello graficamos, lo demás son letreros que se encuentran en la
# gráfica.

# In[108]:


import pandas as pd
from matplotlib import pyplot as plt
x =[1, 2, 3]
y = [1, 4, 9]
z = [10, 5, 0]
plt.plot (x,y)
plt.plot (x,z)
plt.title("Gráfica de ejemplo")
plt.xlabel("x")
plt.ylabel("y y z")
plt.legend(["Datos para y", "Datos para z"])
plt.show()


# 2.- Para esta parte usamos una función de la librería panda para que leyera nuestro archivo.

# In[109]:


data=pd.read_csv('Videojuegos.csv')
data


# 3.- En la siguiente parte del código, usamos "len" para saber de que tamaño es nuestra tabla, y cuántas filas existen

# In[110]:


filas = len(data)
filas


# 4.- Con las siguientes dos partes del código que usan "type", lo usamos para saber de que tipo de variable se está usando

# In[73]:


type (data)


# In[111]:


type (data.Platform)
type (data.Genre)
type (data.Publisher)
type (data.NA_Sales)
type (data.EU_Sales)
type (data.JP_Sales)
type (data.Other_Sales)
type (data.Global_Sales)
type (data.Rating)
type (data.Critic_Score_Class)


# 5.- La siguientes variables que contienen este formato "data.nombre_de_columna", es para analizar las variables y buscar el rancgo
# en el que se encuentra.

# In[75]:


data.Platform


# In[41]:


data.Genre


# In[43]:


data.Publisher


# In[44]:


data.NA_Sales


# In[45]:


data.EU_Sales


# In[46]:


data.JP_Sales


# In[47]:


data.Other_Sales


# In[49]:


data.Global_Sales


# In[50]:


data.Rating


# In[112]:


data.Critic_Score_Class


# 6.- Esta parte que sigue es para conocer cuáles columnas están en nuestra base de datos.

# In[113]:


data.columns


# 7.- El formato siguiente de data.(nombre_de_columna).median, es para calcular la mediana de cada columna que está en la base de 
# datos.

# In[97]:


data['Platform'].median


# In[98]:


data['Genre'].median


# In[99]:


data['Publisher'].median


# In[100]:


data['NA_Sales'].median


# In[101]:


data['EU_Sales'].median


# In[102]:


data['JP_Sales'].median


# In[103]:


data['Other_Sales'].median


# In[104]:


data['Global_Sales'].median


# In[106]:


data['Rating'].median


# In[114]:


data['Critic_Score_Class'].median


# 8.- El siguiente formato de función data(nombre_de_columna).describe es para encontrar ciertas características de cada 
# columna, como la media, mediana, la frecuencia, máximos, mínimos y desviación estandar.

# In[92]:


data['Platform'].describe()


# In[77]:


data['Genre'].describe()


# In[57]:


data['Publisher'].describe()


# In[83]:


data['NA_Sales'].describe()


# In[84]:


data['EU_Sales'].describe()


# In[86]:


data['JP_Sales'].describe()


# In[85]:


data['Other_Sales'].describe()


# In[87]:


data['Global_Sales'].describe()


# In[88]:


data['Rating'].describe()


# In[69]:


data['Critic_Score_Class'].describe()


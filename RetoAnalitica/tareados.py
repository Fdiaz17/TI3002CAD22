#!/usr/bin/env python
# coding: utf-8

# In[141]:


import pandas as pd
import seaborn as sb
import numpy as np; np.random.seed(0)
import matplotlib.pyplot as plt
data = pd.read_csv ('Videojuegos.csv')
datos = pd.read_csv ('Videojuegos.csv')
from matplotlib import cm
plt.rcParams['figure.figsize'] = (16, 9)
plt.style.use('ggplot')
#Voy a revisar dimensiones
data.shape


# In[2]:


data.head()


# In[3]:


data.describe()


# Puedes ver las estadísticas de todos los campos, ayer vimos de uno en particular
# escribir texto de mis datos que sean interesantes.

# # Visualización general

# Eliminar etiquetas de filas o columnas 

# In[95]:


data.drop ([0,1]).hist()
plt.show()


# # Filtros

# In[5]:


mas_de_5 = data[data['Global_Sales']>5]
mas_de_5


# In[20]:


doble_filtro = data[(data['Global_Sales'] > 5) & (data['EU_Sales'] > 1) & (data['JP_Sales'] > 1) & (data['Other_Sales'] > 1)
& (data['NA_Sales'] > 1)]
doble_filtro


# # Visualización

# In[22]:


doble_filtro.set_index('Platform').plot.barh(stacked=True);


# In[27]:


doble_filtro.set_index('Genre').plot.barh(stacked=True);


# In[119]:


df=pd.DataFrame(data['Platform'])
df


# In[202]:


d= data['Global_Sales']
d


# In[52]:


a = "Wii";
k = 0;
for i in df['Platform']:
    if i==a:
        k+=1
print (k)


# In[59]:


b = "WiiU";
z = 0;
for i in df['Platform']:
    if i==b:
        z+=1
print (z)


# In[60]:


c = "DS";
y = 0;
for i in df['Platform']:
    if i==c:
        y+=1
print (y)


# In[61]:


d = "X360";
x = 0;
for i in df['Platform']:
    if i==d:
        x+=1
print (x)


# In[83]:


e = "PS2";
w = 0;
for i in df['Platform']:
    if i==e:
        w+=1
print (w)


# In[65]:


f = "PS3";
v = 0;
for i in df['Platform']:
    if i==f:
        v+=1
print (v)


# In[68]:


g = "PS4";
u = 0;
for i in df['Platform']:
    if i==g:
        u+=1
print (u)


# In[70]:


h = "3DS";
t = 0;
for i in df['Platform']:
    if i==h:
        t+=1
print (t)


# In[72]:


j = "PS";
s = 0;
for i in df['Platform']:
    if i==j:
        s+=1
print (s)


# In[87]:


f2 = "X";
v2 = 0;
for i in df['Platform']:
    if i==f2:
        v2+=1
print (v2)


# In[76]:


f3 = "PC";
v3 = 0;
for i in df['Platform']:
    if i==f3:
        v3+=1
print (v3)


# In[78]:


f4 = "PSP";
v4 = 0;
for i in df['Platform']:
    if i==f4:
        v4+=1
print (v4)


# In[80]:


e1 = "GC";
w1 = 0;
for i in df['Platform']:
    if i==e1:
        w1+=1
print (w1)


# In[81]:


e2 = "GBA";
w2 = 0;
for i in df['Platform']:
    if i==e2:
        w2+=1
print (w2)


# In[84]:


e3 = "XOne";
w3 = 0;
for i in df['Platform']:
    if i==e3:
        w3+=1
print (w3)


# In[98]:


plataformas = ["XOne", "GBA", "GC", "PSP", "PC", "X", "DS", "PS", "3DS", "PS4", "PS2", "PS3", "Wii", "WiiU"]
frecuencia = [169, 249, 363, 401, 734, 586, 472, 154, 161, 255, 1169, 790, 493, 89]
plt.rcParams['figure.figsize'] = (16, 9)
plt.pie(frecuencia, labels=plataformas)
plt.show()


# In[94]:


plt.rcParams['figure.figsize'] = (16, 9)
plt.style.use('ggplot')
data.plot.scatter(x='Platform', y='Global_Sales');


# # Boxplot para otener un diagrama de cajas y bigotes

# In[111]:


plt.rcParams['figure.figsize'] = (16, 9)
data.boxplot(by ='Platform', column =['Global_Sales'], grid = False);


# In[112]:


plt.rcParams['figure.figsize'] = (16, 9)
doble_filtro.boxplot(by ='Platform', column =['Global_Sales'], grid = False);


# In[168]:


plt.rcParams['figure.figsize'] = (16, 9)
sb.boxplot(x ="EU_Sales", y ="JP_Sales", data=doble_filtro);


# In[170]:


# Boxplot
plt.rcParams['figure.figsize'] = (16, 9)
sb.boxplot(data=doble_filtro);


# # Correlación

# In[162]:


data.corr(method = 'pearson')


# In[171]:


data.corr(method = 'kendall')


# # Visualizar mapa de calor

# In[205]:


colormap = plt.cm.viridis
plt.figure(figsize=(12,12))
plt.title('Pearson Correlation of Features', y = 1.05, size = 15)
sb.heatmap(data.corr(),linewidths=0.1, vmax=1.0, square=True,
          cmap=colormap, linecolor= 'white', annot=True);


# In[207]:


normal_data = np.random.randn(20,25)
ax = sb.heatmap(normal_data, center=2)


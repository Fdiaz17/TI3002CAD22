#!/usr/bin/env python
# coding: utf-8

# In[17]:


import pandas as pd
from matplotlib import pyplot as plt


# In[18]:


data1=pd.read_csv('athletes.csv')


# In[20]:


data2=pd.read_csv('countries.csv')


# In[23]:


data3=pd.read_csv('events.csv')


# In[19]:


data1


# In[21]:


data2


# In[24]:


data3


# In[28]:


data1.dtypes


# In[29]:


data2.dtypes


# In[30]:


data3.dtypes


# In[25]:


numero_filas=len(data1)
print("Numero de filas:", numero_filas)


# In[26]:


numero_filas=len(data2)
print("Numero de filas:", numero_filas)


# In[27]:


numero_filas=len(data3)
print("Numero de filas:", numero_filas)


# In[55]:


csv_list=['id', 'name', 'nationality', 'sex', 'dob', 'height', 'weight', 'sport', 'gold', 'silver', 'bronze']
for item in csv_list:
    print(data1[item].describe())


# In[56]:


csv_list=['country', 'code', 'population', 'gdp_per_capita']
for item in csv_list:
    print(data2[item].describe())


# In[57]:


csv_list=['id', 'sport', 'discipline', 'name', 'sex', 'venues']
for item in csv_list:
    print(data3[item].describe())


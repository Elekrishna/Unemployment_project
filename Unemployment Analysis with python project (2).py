#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


# In[3]:


data = pd.read_csv('Unemployment_Rate_upto_11_2020.csv')
data.head()


# In[4]:


data.tail()


# In[5]:


data.shape


# In[6]:


data.info


# In[7]:


data.size


# In[8]:


data.shape


# In[9]:


data.columns


# In[10]:


data.describe


# In[11]:


data.isnull().sum()


# In[12]:


data.duplicated().sum()


# In[13]:


sns.pairplot(data);


# In[14]:


data.columns=['Region', ' Date', ' Frequency', ' Estimated Unemployment Rate (%)',
       ' Estimated Employed', ' Estimated Labour Participation Rate (%)',
       'Region.1', 'longitude', 'latitude']
plt.title("Indian unemployment")
sns.histplot(x=' Estimated Employed', hue="Region.1", data=data)
plt.show()


# In[15]:


data.plot.hist()


# In[16]:


plt.figure(figsize=(12,10))
plt.title('India unemployment')
sns.histplot(x=' Estimated Unemployment Rate (%)',hue='Region',data=data)
plt.show()


# In[17]:


unemploment = data[['Region.1', 'Region',' Estimated Unemployment Rate (%)']]
figure = px.sunburst(unemploment, path=['Region.1', 'Region'], 
                     values=' Estimated Unemployment Rate (%)', 
                     width=700, height=700, color_continuous_scale="RdY1Gn", 
                     title='Unemployment Rate in India')
figure.show()


# In[ ]:





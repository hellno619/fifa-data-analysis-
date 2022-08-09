#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import numpy as np
import seaborn as sns 
from matplotlib import pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[7]:


fifa = pd.read_csv("players_20.csv")


# In[8]:


fifa.head()


# In[9]:


#printing out all the columns
for col in fifa.columns:
    print(col)


# In[10]:


fifa.shape


# In[11]:


fifa['nationality'].value_counts()


# In[16]:


fifa['nationality'].value_counts()[0:5]


# In[17]:


fifa['nationality'].value_counts()[0:5].keys()


# In[18]:


plt.figure(figsize=(8,5))
plt.bar(list(fifa['nationality'].value_counts()[0:5].keys()),list(fifa['nationality'].value_counts()[0:5]),color="g")
plt.show()


# In[19]:


player_salary = fifa[['short_name','wage_eur']]


# In[20]:


player_salary.head()


# In[21]:


player_salary = player_salary.sort_values(by=['wage_eur'],ascending = False)
player_salary.head()


# In[24]:


plt.figure(figsize=(8,5))
plt.bar(list(player_salary['short_name'])[0:5],list(player_salary['wage_eur'])[0:5],color = "y")
plt.show()





# In[26]:


fifa["nationality"] == 'Germany'


# In[27]:


germany = fifa[fifa["nationality"] == 'Germany']
germany.head(10)


# In[30]:


germany.sort_values(by=['height_cm'],ascending=False).head()


# In[31]:


germany.sort_values(by=['wage_eur'],ascending=False).head()


# In[33]:


player_shooting = fifa[["short_name","shooting"]]
player_shooting.sort_values(by=["shooting"],ascending = False).head()


# In[38]:


player_dribbling = fifa[["short_name","dribbling","nationality"]]
player_dribbling.sort_values(by=["dribbling"],ascending = False).head()


# In[40]:


real_madrid = fifa[fifa["club"]=="Real Madrid"]
real_madrid.sort_values(by=["wage_eur"],ascending = False).head()


# In[41]:


real_madrid.sort_values(by=["shooting"],ascending = False).head()


# In[42]:


real_madrid.sort_values(by=["defending"],ascending = False).head()


# In[43]:


real_madrid['nationality'].value_counts()


# In[ ]:





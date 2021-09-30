#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


help(pd.DataFrame)


# In[3]:


list1=[3,-5,7,4]
list2=['a','b','c','d']
series=pd.Series(list1,index=list2)
series


# In[4]:


data_dict = {'Numbers': [1,2,3],
             'Countries': ['DE','FR','IT'],
             'Color': ['Blue','Red','Green']}
df = pd.DataFrame(data=data_dict) 
df


# In[5]:


import numpy as np
ndarray = np.array([(1,2,3),
                    (4,5,6),
                    (7,8,9)])
df2 = pd.DataFrame(ndarray, columns = ['a','b','c']) 
df2


# ## common manipulations
# | Target | Command | Description 
# | --- | --- | --- |
# | adding column (opt.1) | `df['new_col1'] = list` | Adding list to existing DataFrame as a new column at the end | 
# | adding column (opt.2) | `df.insert(2, 'new_col2', list) ` | Insert list to existing DataFrame as a new column at specific position |
# | filter df | `df.filter()` | Select columns or rows by name, regex |
# | filter df by column values (opt.1) | `df.query("Color == 'Blue'")` | Filter based on a query string |
# | filter df by column values (opt.2) | `df[list_bool]` | Filter by a given list of Booleans, like list_bool = [True, False, True, ...] |
# | drop column (opt.1) | `df.drop(columns=['col1', 'col2'])` | Drop column by giving list of column names |
# | drop columns (opt.2) | `df.pop('col_name')` | Drop a column and return the dropped column |
# | drop rows | `df.drop(index=[0,2])` | Drop rows based on list of index |
# | drop NA | `df.dropna()` | Drop the rows where at least one element is missing |
# 

# In[6]:


# will change df!
new_col_list = ['Jan','Feb','Mar']
df['new_col1'] = new_col_list
df


# In[7]:


# will change df!
df.insert(2,'new_col_list2', new_col_list)
df


# In[8]:


# no impact on df, needs to be assigneed
df.filter(items=['Countries','Color'])


# In[9]:


# no impact on df, needs to be assigneed
df.filter(like='ne')


# In[10]:


# no impact on df, needs to be assigneed
df.filter([0,2],axis=0)


# In[11]:


# no impact on df, needs to be assigneed
df.drop(columns=['new_col_list2'])


# In[12]:


# will change df!
df.pop('new_col_list2')


# In[13]:


df.drop(index=2)   


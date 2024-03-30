#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import os


# In[2]:


titanic_train = pd.read_csv(r"C:\Users\hasan\Desktop\INTRO TO ML\WEEK-3\Week-3\train.csv")      # Read the data


# In[3]:


titanic_train.shape


# In[4]:


titanic_train.head(5)


# In[5]:


categorical = titanic_train.dtypes[titanic_train.dtypes == "object"].index
print(categorical)

titanic_train[categorical].describe()


# In[6]:


titanic_train["Ticket"][0:15]


# In[7]:


titanic_train["Ticket"].describe()


# In[8]:


del titanic_train["Ticket"] 


# In[9]:


new_Pclass = pd.Categorical(titanic_train["Pclass"],
                           ordered=True)

new_Pclass = new_Pclass.rename_categories(["Class1","Class2","Class3"])     

new_Pclass.describe()


# In[10]:


titanic_train["Pclass"] = new_Pclass


# In[11]:


titanic_train["Cabin"].unique()


# In[12]:


char_cabin = titanic_train["Cabin"].astype(str) 

new_Cabin = np.array([cabin[0] for cabin in char_cabin]) 

new_Cabin = pd.Categorical(new_Cabin)

new_Cabin .describe()


# In[13]:


titanic_train["Cabin"] = new_Cabin


# In[14]:


dummy_vector = pd.Series([1,None,3,None,7,8])

dummy_vector.isnull()


# In[15]:


titanic_train["Age"].describe()


# In[16]:


missing = np.where(titanic_train["Age"].isnull() == True)
missing


# In[17]:


len(missing[0])


# In[18]:


titanic_train.hist(column='Age',    
                   figsize=(9,6),   
                   bins=20)         


# In[19]:


new_age_var = np.where(titanic_train["Age"].isnull(), 
                       28,                       
                       titanic_train["Age"])     

titanic_train["Age"] = new_age_var 

titanic_train["Age"].describe()


# In[20]:


titanic_train.hist(column='Age',    
                   figsize=(9,6),   
                   bins=20)         


# In[ ]:





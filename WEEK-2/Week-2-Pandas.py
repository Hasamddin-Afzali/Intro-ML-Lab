#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np 
import pandas as pd


# In[2]:


t = (1,2,3,4)
t[1:3]


# In[3]:


dictionary = {"name":["ali","veli","zübeyde","ahmet","kubra","can"],
             "age":[12,34,56,78,None,12],
             "note":[123,456,78,87654,None,89]}
dataframe1 = pd.DataFrame(dictionary) 
print(dataframe1)


# In[4]:


df = pd.read_csv(r"C:\Users\hasan\Desktop\INTRO TO ML\WEEK-2\WEEK-2\data.csv")
print(df)


# In[5]:


head = dataframe1.head() 
print(head)


# In[6]:


tail = dataframe1.tail()
print(tail)


# In[7]:


print(dataframe1.columns)


# In[8]:


print(dataframe1.info())


# In[9]:


print(dataframe1.dtypes)


# In[10]:


print(dataframe1.describe())


# In[14]:


print(dataframe1["name"]) 
print(dataframe1.loc[:, "age"])            
dataframe1["new_future"] = [1,2,3,4,5,6] 
print(dataframe1.loc[:3,"age"])
print(dataframe1.loc[:3, "name":"note"])
print(dataframe1.loc[::-1])


# In[20]:


print(dataframe1.loc[:"new_feature"])


# In[21]:


print(dataframe1.loc[:3, ["name","note"]])


# In[22]:


print(dataframe1.loc[:,:"age"])


# In[23]:


print(dataframe1.iloc[:,[2]])


# In[24]:


filtre1 = dataframe1.age>10
dataframe1["bool"]= filtre1
print(dataframe1.loc[:,["age","bool"]])


# In[26]:


type(filtre1)


# In[27]:


filtrelenmis_data= dataframe1[filtre1] 
print(filtrelenmis_data)


# In[28]:


filtre2 = dataframe1.note>100
filtrelenmis_data2 = dataframe1[filtre2&filtre1] 
print(filtrelenmis_data2)


# In[29]:


dataframe1[dataframe1.age>20]


# In[30]:


mean1 = dataframe1.note.mean()
print(mean1)
mean_np= np.mean(dataframe1.note) 
print(mean_np)


# In[31]:


dataframe1.dropna(inplace=True) 
dataframe1


# In[32]:


print(dataframe1.note.mean())
dataframe1["mean"]= ["bad" if dataframe1.note.mean()>each else "good" for each in dataframe1.note]
dataframe1


# In[33]:


dataframe1.columns = [each.upper() for each in dataframe1.columns] 

dataframe1.columns


# In[34]:


dataframe1.drop(["NEW_FUTURE"],axis=1,inplace=True)
dataframe1


# In[35]:


data1 = dataframe1.head()     
data2 = dataframe1.tail()
data_concat = pd.concat([data1,data2],axis=0)
data_concat


# In[36]:


data_contact2 = pd.concat([data1,data2],axis=1)
data_contact2


# In[37]:


dataframe1["new_age"] = [each*2 for each in dataframe1.AGE]
dataframe1


# In[ ]:





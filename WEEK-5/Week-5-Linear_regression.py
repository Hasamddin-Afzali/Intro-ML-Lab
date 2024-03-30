#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# In[2]:


df=pd.read_csv(r"C:\Users\hasan\Desktop\INTRO TO ML\WEEK-5\linear_regression_dataset.csv")


# In[3]:


df


# In[4]:


df=pd.read_csv(r"C:\Users\hasan\Desktop\INTRO TO ML\WEEK-5\linear_regression_dataset.csv", sep=";")


# In[5]:


df


# In[6]:


plt.scatter(df.deneyim,df.maas)
plt.xlabel("experience")
plt.ylabel("salary")
plt.show()


# In[7]:


x=df.deneyim.values


# In[8]:


x.shape


# In[9]:


x=df.deneyim.values.reshape(-1,1)
y=df.maas.values.reshape(-1,1)


# In[10]:


from sklearn.linear_model import LinearRegression
linear_reg=LinearRegression()
linear_reg.fit(x,y)


# In[11]:


b0=linear_reg.predict([[0]])


# In[12]:


b0=linear_reg.intercept_
print(b0)


# In[13]:


b1=linear_reg.coef_
print(b1)


# Y=BO+B1*X

# In[14]:


new_salary=1663+1138*11
print(new_salary)


# In[15]:


b11=linear_reg.predict([[11]])
print(b11)


# In[16]:


y_head=linear_reg.predict(x)
plt.plot(x,y_head,color="red")
plt.scatter(x,y)
plt.show()


# In[17]:


from sklearn.metrics import r2_score
print("r square score",r2_score(y,y_head))


# In[ ]:





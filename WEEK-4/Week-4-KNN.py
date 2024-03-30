#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


data=pd.read_csv(r"C:\Users\hasan\Desktop\INTRO TO ML\WEEK-4\Week-4\data.csv")


# In[3]:


data.head()


# In[4]:


data.info()


# In[5]:


data.drop(["Unnamed: 32","id"],axis=1,inplace=True)


# In[6]:


M =data[data.diagnosis=="M"]
B =data[data.diagnosis=="B"]


# In[7]:


M.info()


# In[8]:


B.info()


# In[9]:


plt.scatter(M.radius_mean,M.area_mean,color="red",label="malignant")
plt.scatter(B.radius_mean,B.area_mean,color="green",label="benign")
plt.legend()
plt.xlabel("radius_mean")
plt.ylabel("area_mean")
plt.show()


# In[10]:


plt.scatter(M.radius_mean,M.texture_mean,color="red",label="malignant")
plt.scatter(B.radius_mean,B.texture_mean,color="green",label="benign")
plt.legend()
plt.xlabel("radius_mean")
plt.ylabel("texture_mean")
plt.show()


# In[11]:


data.diagnosis=[1 if each=="M" else 0 for each in data.diagnosis]


# In[12]:


data.diagnosis


# In[13]:


y=data.diagnosis.values


# In[14]:


x_data=data.iloc[:,1:3].values


# In[15]:


x=(x_data - np.min(x_data))/(np.max(x_data)-np.min(x_data))


# In[16]:


from  sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3,random_state=1)


# In[17]:


from sklearn.neighbors import KNeighborsClassifier
knn=KNeighborsClassifier(n_neighbors=3)
knn.fit(x_train,y_train)


# In[18]:


y_head=knn.predict(x_test)
y_head


# In[19]:


print("when k is {}, accuracy of KNN classification {} " .format(3,knn.score(x_test,y_test)))


# In[20]:


test_accuracy=[]
for each in range(1,15):
    knn2=KNeighborsClassifier(n_neighbors=each)
    knn2.fit(x_train,y_train)
    test_accuracy.append(knn2.score(x_test,y_test))

plt.figure(figsize=(5,5))
plt.plot(range(1,15),test_accuracy)
plt.title("k values vs accuracy")
plt.xlabel("k labels")
plt.xlabel("accuracy")
plt.grid()
plt.show()
print("best accuracy is {} with K ={}".format(np.max(test_accuracy),1+test_accuracy.index(np.max(test_accuracy))))


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Importing the libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


#Reading the dataset
data = pd.read_csv(r"C:\Users\hasan\Desktop\INTRO TO ML\WEEK-5\Week-5\advertising.csv")


# In[3]:


data.head()


# In[4]:


X = data[['TV', 'Radio', 'Newspaper']]
y = data['Sales']


# In[5]:


from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 100)


# In[6]:


from sklearn.linear_model import LinearRegression
mlr = LinearRegression()  
mlr.fit(X_train, y_train)


# In[7]:


print("Intercept: ", mlr.intercept_)
print("Coefficients:")
list(zip(X, mlr.coef_))


# In[8]:


#Prediction of test set
y_pred_mlr= mlr.predict(X_test)
#Predicted values
print("Prediction for test set: {}".format(y_pred_mlr))


# In[9]:


#Actual value and the predicted value
mlr_diff = pd.DataFrame({'Actual value': y_test, 'Predicted value': y_pred_mlr})
mlr_diff.head()


# In[10]:


#Model Evaluation
from sklearn import metrics
meanSqErr = metrics.mean_squared_error(y_test, y_pred_mlr)
print('R squared: {:.2f}'.format(mlr.score(X,y)*100))
print('Mean Square Error:', meanSqErr)


# In[ ]:





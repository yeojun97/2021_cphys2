#!/usr/bin/env python
# coding: utf-8

# In[23]:


from sklearn import datasets
diabetes=datasets.load_diabetes()


# In[24]:


X_age=diabetes.data[:,0] #나이
X_bmi=diabetes.data[:,2] #BMI
X_p=diabetes.data[:,3] #혈압
Y = diabetes.target


# In[27]:


import matplotlib.pyplot as plt
plt.scatter(diabetes.data[:,0],diabetes.target)
plt.xlabel('Age')
plt.ylabel('diabetes.target')
plt.show


# In[28]:


import matplotlib.pyplot as plt
plt.scatter(diabetes.data[:,2],diabetes.target)
plt.xlabel('BMI')
plt.ylabel('diabetes.target')
plt.show


# In[30]:


import matplotlib.pyplot as plt
plt.scatter(diabetes.data[:,3],diabetes.target)
plt.xlabel('Blood pressure')
plt.ylabel('diabetes.target')
plt.show


# In[33]:


from sklearn.linear_model import LinearRegression


# In[34]:


import numpy as np
import matplotlib.pyplot as plt


# In[58]:


x = np.array(diabetes.data[:,0])
y = np.array(diabetes.target)

X = np.array([[i] for i in x])
Y = np.array([[i] for i in y])
plt.plot(x,y,'o')

f=LinearRegression()
f.fit(X,Y)

f.coef_, f.intercept_


# In[51]:


plt.plot(x,y,'o')
plt.plot(x,f.predict(X))
plt.xlabel('Age')
plt.ylabel('diabetes.target')


# In[57]:


x = np.array(diabetes.data[:,2])
y = np.array(diabetes.target)

X = np.array([[i] for i in x])
Y = np.array([[i] for i in y])
plt.plot(x,y,'o')

f=LinearRegression()
f.fit(X,Y)

f.coef_, f.intercept_


# In[50]:


plt.plot(x,y,'o')
plt.plot(x,f.predict(X))
plt.xlabel('BMI')
plt.ylabel('diabetes.target')


# In[56]:


x = np.array(diabetes.data[:,3])
y = np.array(diabetes.target)

X = np.array([[i] for i in x])
Y = np.array([[i] for i in y])
plt.plot(x,y,'o')

f=LinearRegression()
f.fit(X,Y)

f.coef_, f.intercept_


# In[53]:


plt.plot(x,y,'o')
plt.plot(x,f.predict(X))

plt.xlabel('Blood pressure')
plt.ylabel('diabetes.target')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





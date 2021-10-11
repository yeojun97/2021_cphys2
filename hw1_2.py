#!/usr/bin/env python
# coding: utf-8

# In[24]:


from sklearn import datasets
diabetes=datasets.load_diabetes()


# In[25]:


X_age=diabetes.data[:,0] #나이
X_bmi=diabetes.data[:,2] #BMI
X_p=diabetes.data[:,3] #혈압
Y = diabetes.target


# In[26]:


import matplotlib.pyplot as plt
import numpy as np
x = np.array(diabetes.data[:,0])
y = np.array(diabetes.target)

X = np.array([[i] for i in x])
Y = np.array([[i] for i in y])
plt.plot(x,y,'o')
Z = np.arange(-0.11,0.11,0.0001)

a, b = 250, 120

plt.plot(Z,a*Z+b)


# In[27]:


y_hat = a*x+b
y_hat


# In[28]:


np.mean((y_hat-y)**2)


# In[29]:


def mse(a,b,y):
    y_hat=a*x+b
    return np.mean((y_hat-y)**2)


# In[30]:


a=250; b=120;
mse(a,b,y)


# In[31]:


eps = 5
mse(a+eps,b,y),mse(a-eps,b,y)
mse(a,b+eps,y), mse(a, b-eps, y)


# In[32]:


eps=0.2
n=0;
while(n<50000):
    if(mse(a+eps,b,y)>mse(a-eps,b,y)):
        a=a-eps
    else:
        a=a+eps
    
    if(mse(a,b+eps,y)>mse(a,b-eps,y)):
        b=b-eps
    else:
        b=b+eps
    n=n+1


# In[33]:


a,b


# In[35]:


def f(a,b,Z):
    return a*Z+b

plt.plot(x,y,'o')
plt.plot(Z,f(a,b,Z))
plt.xlabel('Age')
plt.ylabel('diabetes.target')


# In[54]:


import matplotlib.pyplot as plt
import numpy as np
x = np.array(diabetes.data[:,2])
y = np.array(diabetes.target)

X = np.array([[i] for i in x])
Y = np.array([[i] for i in y])
plt.plot(x,y,'o')
Z = np.arange(-0.095,0.17,0.0001)

a, b = 900, 170

plt.plot(Z,a*Z+b)


# In[55]:


y_hat = a*x+b
y_hat


# In[56]:


np.mean((y_hat-y)**2)


# In[57]:


def mse(a,b,y):
    y_hat=a*x+b
    return np.mean((y_hat-y)**2)


# In[58]:


a=900; b=170;
mse(a,b,y)


# In[59]:


eps = 5
mse(a+eps,b,y),mse(a-eps,b,y)
mse(a,b+eps,y), mse(a,b-eps,y)


# In[60]:


eps=0.2
n=0;
while(n<50000):
    if(mse(a+eps,b,y)>mse(a-eps,b,y)):
        a=a-eps
    else:
        a=a+eps
    
    if(mse(a,b+eps,y)>mse(a,b-eps,y)):
        b=b-eps
    else:
        b=b+eps
    n=n+1


# In[61]:


a,b


# In[62]:


def f(a,b,Z):
    return a*Z+b

plt.plot(x,y,'o')
plt.plot(Z,f(a,b,Z))
plt.xlabel('BMI')
plt.ylabel('diabetes.target')


# In[120]:


import matplotlib.pyplot as plt
import numpy as np
x = np.array(diabetes.data[:,3])
y = np.array(diabetes.target)

X = np.array([[i] for i in x])
Y = np.array([[i] for i in y])
plt.plot(x,y,'o')
Z = np.arange(-0.115,0.135,0.0001)

a, b = 760, 160

plt.plot(Z,a*Z+b)


# In[121]:


y_hat = a*x+b
y_hat


# In[122]:


np.mean((y_hat-y)**2)


# In[123]:


def mse(a,b,y):
    y_hat=a*x+b
    return np.mean((y_hat-y)**2)


# In[124]:


a=750; b=150;
mse(a,b,y)


# In[125]:


eps = 5
mse(a+eps,b,y),mse(a-eps,b,y)
mse(a,b+eps,y), mse(a,b-eps,y)


# In[126]:


eps=0.2
n=0;
while(n<50000):
    if(mse(a+eps,b,y)>mse(a-eps,b,y)):
        a=a-eps
    else:
        a=a+eps
    
    if(mse(a,b+eps,y)>mse(a,b-eps,y)):
        b=b-eps
    else:
        b=b+eps
    n=n+1


# In[127]:


a,b


# In[128]:


def f(a,b,Z):
    return a*Z+b

plt.plot(x,y,'o')
plt.plot(Z,f(a,b,Z))
plt.xlabel('BMI')
plt.ylabel('diabetes.target')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





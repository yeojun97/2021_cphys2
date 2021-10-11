#!/usr/bin/env python
# coding: utf-8

# In[8]:


import numpy as np
import matplotlib.pyplot as plt


# In[9]:


x = np.arange(-10,10,0.01)
def f(x):
    return 0.5*x**4 - 3*x**3
plt.ylim(-100,100)
plt.xlim(-5,7)
plt.plot(x,f(x))


# In[14]:


x_A = 0
x_B = 6
eps = 0.01
precision = 0.00001

def fp(x):
    return 2*x**3 - 9*x**2

x_C = []
for i in range(1000):
    x_A = x_B
    x_B = x_A - eps*fp(x_A)
    x_C.append(x_B)
    if abs(x_B - x_A) < precision: break
        
print("최소값" + str(min(x_C)))


# In[ ]:





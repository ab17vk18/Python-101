#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#PYTHON DEBUGGER - pdb


# In[3]:


import pdb


# In[5]:


a = [1,3,5]
b = 2
c = 4

result = b + c
print(result)

pdb.set_trace()  #Implementing trace - Interactive debugging environment

result2 = a**2 #Introducing error on purpose
print(result2)


# In[ ]:





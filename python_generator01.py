#!/usr/bin/env python
# coding: utf-8

# In[1]:


#PYTHON GENERATORS: Generates sequences as and when needed instead of accumulating memory


# In[7]:


def create_cubes(n):
    result = []
    for i in range(1,n+1):
        result.append(i**3)
    return result


# In[10]:


l = create_cubes(10)


# In[12]:


for num in l:    #Prints one value at a time, so creating an entire list of all possible values is memory inefficient
    print(num)


# In[13]:


#SAME FUNCTION MODIFIED USING GENERATORS - WAY MORE MEMORY EFFICIENT

def create_cubes(n):
    for i in range(1,n+1):
        yield i**3


# In[14]:


create_cubes(10)


# In[15]:


for num in create_cubes(10):
    print(num)


# In[16]:


#Generators can be casted as list:

l = list(create_cubes(10))


# In[18]:


print(l)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





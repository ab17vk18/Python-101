#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1) Create a generator that generates the squares of numbers up to some number N


# In[2]:


def gensquares(N):

    for i in range(N):
        yield i*i


# In[3]:


for x in gensquares(10):
    print(x)


# In[ ]:





# In[4]:


#2) Create a generator that yields "n" random numbers between a low and high number (that are inputs).
##Note: Use the random library


# In[7]:


import random

def rand_num(low,high,n):

    for i in range(n):
        yield random.randint(low,high)  #Uses 'randint' attribute that is defined in the 'random' library


# In[8]:


for num in rand_num(1,10,12):
    print(num)


# In[ ]:





# In[9]:


#3) Use the iter() function to convert a string into an iterator


# In[16]:


s = "What's up, dawg?"

s_iterator = iter(s)


# In[17]:


for i in range(len(s)):
    print(next(s_iterator))


# In[18]:


next(s_iterator)


# In[ ]:





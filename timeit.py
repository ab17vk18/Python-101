#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#TIMEIT - To check how long a piece of code executes


# In[4]:


import timeit


# In[5]:


'0-1-2-3....-99'


# In[6]:


'-'.join(str(n) for n in range(100))


# In[13]:


timeit.timeit('"-".join(str(n) for n in range(100))',number=10000)


# In[14]:


timeit.timeit('"-".join([str(n) for n in range(100)])',number=10000)


# In[16]:


timeit.timeit('"-".join(map(str,range(100)))',number=10000)


# In[18]:


map(str,range(100))


# In[19]:


#TIMEIT  magic function to check each execution


# In[21]:


get_ipython().run_line_magic('timeit', '"-".join(str(n) for n in range(100))')


# In[22]:


get_ipython().run_line_magic('timeit', '"-".join([str(n) for n in range(100)])')


# In[23]:


get_ipython().run_line_magic('timeit', '"-".join(map(str,range(100)))')


# In[ ]:





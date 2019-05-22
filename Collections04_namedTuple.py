#!/usr/bin/env python
# coding: utf-8

# In[1]:


#COLLECTIONS - 04) Named tuple - subclass of tuple, creates a name and an index for every value


# In[2]:


t = (2,'Lab','Sammy')


# In[3]:


t


# In[4]:


t[0]


# In[5]:


t[1]


# In[6]:


t[2]


# In[15]:


type(t)


# In[7]:


from collections import namedtuple


# In[8]:


Dog = namedtuple('Dog','age breed name')


# In[10]:


d = Dog(age=2,breed='Lab',name='Sammy')


# In[11]:


d.age


# In[12]:


d.breed


# In[13]:


d.name


# In[14]:


type(d)


# In[16]:


Car = namedtuple('Car','brand price abs')


# In[17]:


c = Car('Porsche',60000,False)


# In[18]:


c.abs


# In[19]:


c.brand


# In[20]:


c.price


# In[ ]:





# In[ ]:





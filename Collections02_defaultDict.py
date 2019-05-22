#!/usr/bin/env python
# coding: utf-8

# In[22]:


#COLLECTIONS - 02)Default Dictionary - Assigns and initialise any key with default value,thus does not throw KeyError


# In[2]:


from collections import defaultdict


# In[4]:


d = {'k1':0} #A normal dictionary


# In[5]:


d['k1']


# In[7]:


d['k2'] #Throws key error since 'k2' key doesnt exist


# In[8]:


d = defaultdict(object)


# In[9]:


d['k1']  #Assigns a default value for the key, so doesnt throw error


# In[10]:


d['k2']


# In[11]:


d['k1'] = 1 #Assigning manual value for a given key


# In[15]:


for item in d:
    print(item)


# In[16]:


d


# In[17]:


d = defaultdict(lambda:0)  #Assigns any key a default value of 0 using through the lambda expression


# In[18]:


d['k1']


# In[19]:


d['k2'] = 2


# In[20]:


d ['k3']


# In[21]:


d


# In[ ]:





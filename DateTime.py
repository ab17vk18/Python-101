#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Datetime module - Used primarily to create timestamps and extract the time


# In[2]:


import datetime


# In[6]:


t = datetime.time(5,30,0)  #datetime.time(hh:mm:ss:ms)


# In[5]:


print(t)


# In[7]:


t.hour


# In[8]:


t.minute


# In[12]:


print (datetime.time.min)


# In[13]:


print (datetime.time.max)


# In[14]:


print (datetime.time.resolution)


# In[15]:


today = datetime.date.today()


# In[16]:


print(today)


# In[17]:


today.year


# In[18]:


today.month


# In[19]:


today.day


# In[27]:


d1 = datetime.date(2017,12,31)


# In[28]:


d2 = d1.replace(year=1997)


# In[29]:


print(d2)


# In[31]:


print(d1 - d2)


# In[ ]:





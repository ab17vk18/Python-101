#!/usr/bin/env python
# coding: utf-8

# In[1]:


#COLLECTIONS - 03) Ordered dictionary - Retains the order in which key-val pairs are added


# In[38]:


d = {}

d['a'] = 1
d['b'] = 2
d['e'] = 5
d['c'] = 3
d['h'] = 8
d['z'] = 26
d['k'] = 11


# In[39]:


d


# In[40]:


for k,v in d.items():
    print(k,v)        #Supposedly does not retain the order in which elements are added


# In[42]:


import collections

d = collections.OrderedDict()


# In[43]:


d['d'] = 4
d['a'] = 1
d['b'] = 2
d['e'] = 5
d['c'] = 3
d['h'] = 8
d['z'] = 26
d['k'] = 11


# In[44]:


for k,v in d.items():
    print(k,v)         #Ordered Dictionary retains the order in which elements are added


# In[48]:


#The below cells illustrate the difference between dictionary and ordered dictionary


# In[46]:


d1 = {}
d1['a'] = 1
d1['b'] = 2

d2 = {}
d2['b'] = 2
d2['a'] = 1

print (d1==d2)


# In[47]:


od1 = collections.OrderedDict()
od1['a'] = 1
od1['b'] = 2

od2 = collections.OrderedDict()
od2['b'] = 2
od2['a'] = 1

print (od1==od2)


# In[ ]:





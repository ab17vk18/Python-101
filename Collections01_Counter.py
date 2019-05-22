#!/usr/bin/env python
# coding: utf-8

# In[1]:


#COLLECTIONS MODULE: 01)Counter - return count of elements in the form of dictionary


# In[2]:


from collections import Counter


# In[3]:


s = [1,2,3,1,2,3,1,2,1,2,1,1,2,2,3,4,5,3,4,5,3,4,4,4,5,5,5,5,5]


# In[6]:


Counter(s)


# In[7]:


c = Counter(s)


# In[12]:


c.most_common(1)   #Returns ordered list of most common items


# In[13]:


l = 'Peter Piper picked a peck of pickled peppers A peck of pickled peppers Peter Piper picked If Peter Piper picked a peck of pickled peppers Where’s the peck of pickled peppers Peter Piper picked?'


# In[16]:


c = Counter(l.lower())


# In[17]:


c


# In[18]:


words = l.split()


# In[22]:


count = Counter(words)


# In[23]:


count


# In[24]:


sum(count.values())   #Returns total count


# In[ ]:





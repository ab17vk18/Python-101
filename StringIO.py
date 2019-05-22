#!/usr/bin/env python
# coding: utf-8

# In[1]:


#StringIO - To create in-memory file-like objects within your program that Python treats the same way as a file:


# In[2]:


import io


# In[3]:


# Arbitrary String
message = 'This is just a normal string.'


# In[4]:


# Use StringIO method to set as file object
f = io.StringIO(message)


# In[5]:


f.read() #Performs read on the StringIO object


# In[7]:


f.write(' Second line written to file like object')   #Write can also be performed on the StringIO object


# In[8]:


# Reset cursor just like you would a file
f.seek(0)


# In[9]:


# Read again
f.read()


# In[10]:


# Close the object when contents are no longer needed
f.close()


# In[ ]:





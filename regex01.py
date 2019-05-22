#!/usr/bin/env python
# coding: utf-8

# In[5]:


#REGULAR EXPRESSIONS: regex01


# In[6]:


import re


# In[4]:


patterns = ['term1','term2']

text = 'This is the text that contains term1 but not the other term'


# In[14]:


for pattern in patterns:
    
    print(f"Searching for '{pattern}':")
    if re.search(pattern,text):   #Returns match object
        print("Match for '{}' found in '{}'\n".format(pattern,text))
    
    else:
        print('No match found\n')


# In[21]:


match = re.search(patterns[0],text)


# In[22]:


print(match)


# In[23]:


match.start()


# In[24]:


match.end()


# In[25]:


match.span()


# In[26]:


split_term = '@'

phrase = 'terribleawesome@gmail.com'


# In[27]:


re.split(split_term,phrase)


# In[29]:


phrase.split('@')


# In[30]:


string = "I Scream. I scream you scream, let's all scream, for ice cream!"


# In[32]:


occ = re.findall('scream',string.lower())


# In[33]:


print(occ)


# In[36]:


print('Total number of occurances: ',len(occ))


# In[ ]:





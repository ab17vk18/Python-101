#!/usr/bin/env python
# coding: utf-8

# In[1]:


#CREATING FIBONACCI SERIES USING GENERATOR:


# In[17]:


def gen_fibonacci(n):
    
    a = 1
    b = 1
    for i in range(n):
        yield a
        a,b = b,a+b   #This is not equal to assigning a=b and then b=a+b
        
        ##The above tuple matching a,b=b,a+b is similar to the below three lines of code:
        #x = a
        #a = b
        #b = x+b


# In[18]:


for num in gen_fibonacci(10):
    print(num)


# In[19]:


#NEXT FUNCTION AND ITER FUNCTION:


# In[38]:


#NEXT FUNCTION:

def simple_gen(n):
    
    for i in range(n):
        yield i


# In[39]:


g = simple_gen(3)


# In[40]:


next(g)


# In[41]:


next(g)


# In[42]:


next(g)


# In[44]:


next(g)   #StopIteration error occurs if next() is called beyond what the generator generates


# In[46]:


#ITER FUNCTION - To iterate using next() on a non-iterable object such as string, can be iterated only through for loop

s = 'Hello'

for letter in s:
    print(letter)


# In[49]:


next(s)  #Throws TypeError as str is not an iterator object


# In[57]:


s_iter = iter(s)   #Casting str to iter to allow iteration


# In[58]:


next(s_iter)


# In[59]:


next(s_iter)


# In[60]:


next(s_iter)


# In[61]:


next(s_iter)


# In[62]:


next(s_iter)


# In[63]:


next(s_iter)


# In[ ]:





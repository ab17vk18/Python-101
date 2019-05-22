#!/usr/bin/env python
# coding: utf-8

# In[1]:


def func():
    return 1


# In[2]:


func()


# In[3]:


func


# In[4]:


def hello():
    print('Hello')


# In[5]:


hello


# In[6]:


greet = hello


# In[7]:


greet()


# In[9]:


hello()


# In[11]:


del hello


# In[12]:


hello()


# In[13]:


greet()


# In[ ]:





# In[ ]:





# In[ ]:





# In[16]:


def hello(name='default'):
    
    print("Inside hello() function")
    
    def welcome():
        return '\tInside welcome() within hello()'
    
    def greet():
        return '\tInside greet() within hello()'
    
    print(welcome())
    print(greet())
    print("End of hello() function")
    


# In[17]:


hello()


# In[18]:


def hello(name='default'):
    
    print("Inside hello() function")
    
    def welcome():
        return '\tInside welcome() within hello()'
    
    def greet():
        return '\tInside greet() within hello()'
    
    print("Hey! Im going to return a function")
    if name=='default':
        return welcome
    else:
        return greet
    
    print("End of hello() function")


# In[19]:


my_new_func = hello('default')


# In[21]:


print(my_new_func())


# In[22]:


my_another_func = hello('pro')


# In[23]:


print(my_another_func())


# In[24]:


def cool():
    
    def super_cool():
        print("super_cool() executed")
        
    return super_cool


# In[25]:


super_cool = cool()


# In[26]:


super_cool()


# In[27]:


super_cool


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[30]:


def hello():
    return "Hello. Inside hello() function"


# In[33]:


def otherfunc(argument_func):
    print("hi...")
    print(argument_func())


# In[34]:


otherfunc(hello)


# In[ ]:





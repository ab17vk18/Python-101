#!/usr/bin/env python
# coding: utf-8

# In[14]:


#ILLUSTRATION OF HOW DECORATORS AND HOW @ ACTS AS A SWITCH TO TOGGLE BETWEEN ORIGINAL FUNCTION AND DECORATED FUNCTION


# In[1]:


def new_decorator_func(original_func_temp):
    
    def decorated_func():
        
        print("Some codes being executed before the original function")
        print("Going to execute original function\n")
        original_func_temp()
        print("\nOriginal function executed")
        print("Executing some codes after the original function")
        
    return decorated_func


# In[2]:


def original_func():
    
    print("HEY! THIS IS THE ORIGINAL CODES")


# In[3]:


original_func()


# In[6]:


decorated_func = new_decorator_func(original_func)


# In[8]:


print(decorated_func())


# In[16]:


@new_decorator_func
def original_func():
    
    print("HEY! THIS IS THE ORIGINAL CODES")


# In[17]:


original_func()


# In[19]:


#@new_decorator_func    #COMMENTING @ TO RETURN TO THE ORIGINAL FUNCTION
def original_func():
    
    print("HEY! THIS IS THE ORIGINAL CODES")


# In[20]:


original_func()


# In[ ]:





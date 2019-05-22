#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Error handling:


# In[2]:


def addition(a,b):
    return a+b


# In[4]:


addition(10,20)


# In[12]:


a = 10
b = input("Enter the second number: ")


# In[8]:


addition(a,b)  #throws error as b is accepted as a string, not as an integer


# In[15]:


#TRY-EXCEPT-ELSE code block to illustrate error handling:

try:
    #Block of code that is bound to throw an error
    
    result = 10 + '10'
    
except:
    print("Hey! You haven't entered integer")
    
else:
    print("Addition went well, here's the result: {}".format(result))


# In[30]:


#Using FINALLY(this always runs regardless of error):

try:
    f = open('testfile','r')   #Throw OSError as the user is trying to write the file which is opened in read mode
    f.write("This is testfile")
    f.close()
except TypeError:
    print("Oops! Looks like there is a datatype mismatch")
except OSError:
    print("Something wrong! You have an OS Error")
except:
    print("All other exceptions")
finally:
    print("I always run. Thank you")


# In[ ]:





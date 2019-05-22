#!/usr/bin/env python
# coding: utf-8

# # Errors and Exceptions Homework

# ### Problem 1
# Handle the exception thrown by the code below by using <code>try</code> and <code>except</code> blocks.

# In[1]:


try:
    for i in ['a','b','c']:
        print(i**2)
        
except TypeError:
    print("Squaring a string is mathematically impossible")
    


# ### Problem 2
# Handle the exception thrown by the code below by using <code>try</code> and <code>except</code> blocks. Then use a <code>finally</code> block to print 'All Done.'

# In[3]:


x = 5
y = 0

try:
    z = x/y

except ZeroDivisionError:
    print("Come on, mate! You can't divide by zero.")
    
finally:
    print("All Done")


# ### Problem 3
# Write a function that asks for an integer and prints the square of it. Use a <code>while</code> loop with a <code>try</code>, <code>except</code>, <code>else</code> block to account for incorrect inputs.

# In[4]:


def ask():
    
    while True:
        try:
            number = int(input("Input an integer: "))
            square = number ** 2
    
        except:
            print("An error occured! Please try again!")
            continue
    
        else:
            print("Thank you, your number square is: {}".format(square))
            break
    


# In[5]:


ask()


# # Great Job!

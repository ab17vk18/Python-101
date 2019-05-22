#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Asks for 10 digit phone number from the user and verifies the same using Exception Handling

def ask_phone():
   
    while True:
        try:
            phone = int(input("Please enter your 10 digit phone number: "))
            if phone >= 1000000000 and phone < 10000000000:
                print("You've entered: {}".format(phone))
            else:
                raise TypeError('***')
                continue
    
        except:
            print("Whoops! That's not a phone number. Please try again.")
            continue
    
        else:
            print("Your phone number is accepted")
            break
    
        finally:
            print("Thank You\n")


# In[3]:


ask_phone()


# In[4]:


ask_phone()


# In[ ]:





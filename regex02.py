#!/usr/bin/env python
# coding: utf-8

# In[27]:


#REGULAR EXPRESSIONS 02:


# In[28]:


import re


# In[29]:


def multi_re_find(patterns,phrase):
        '''
        Takes in a list of regex patterns
        Prints a list of all matches
        '''
        for pattern in patterns:
            print("Searching the phrase using the re check: '{}'" .format(pattern))
            print(re.findall(pattern,phrase))
            print('\n')


# In[30]:


#Repetition syntax:


# In[31]:


test_phrase = 'sdsd..sssddd...sdddsddd...dsds...dsssss...sdddd'

test_patterns = ['sd*',         # s followed by zero or more d's
                'sd+',          # s followed by one or more d's
                'sd?',          # s followed by zero or one d's
                'sd{3}',        # s followed by three d's
                'sd{2,3}',      # s followed by two to three d's
                ]

multi_re_find(test_patterns,test_phrase)


# In[32]:


#Character Sets:


# In[33]:


test_phrase = 'sdsd..sssddd...sdddsddd...dsds...dsssss...sdddd'

test_patterns = ['[sd]',    # either s or d
                's[sd]+']   # s followed by one or more s or d

multi_re_find(test_patterns,test_phrase)


# In[34]:


#Exclusion:


# In[35]:


test_phrase = 'This is a string! But it has punctuation. How can we remove it?'


# In[36]:


#[^!.? ]to check for matches that are not a !,.,?, or space. Add a '+' to check that the match appears at least once.


# In[37]:


re.findall('[^!.? ]+',test_phrase)


# In[38]:


#Character Ranges:


# In[39]:


test_phrase = 'This is an example sentence. Lets see if we can find some letters.TADA!'

test_patterns=['[a-z]+',      # sequences of lower case letters
               '[A-Z]+',      # sequences of upper case letters
               '[a-zA-Z]+',   # sequences of lower or upper case letters
               '[A-Z][a-z]+'] # one upper case letter followed by lower case letters
                
multi_re_find(test_patterns,test_phrase)


# In[40]:


#Escape Sequences:


# In[41]:


test_phrase = 'This is a string with some numbers 1233 and a symbol #hashtag'

test_patterns=[ r'\d+', # sequence of digits
                r'\D+', # sequence of non-digits
                r'\s+', # sequence of whitespace
                r'\S+', # sequence of non-whitespace
                r'\w+', # alphanumeric characters
                r'\W+', # non-alphanumeric
                ]

multi_re_find(test_patterns,test_phrase)


# In[ ]:





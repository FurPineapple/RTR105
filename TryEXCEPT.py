#!/usr/bin/env python
# coding: utf-8

# In[1]:


astr=input("Please enter a num: ")
try:
    istr=int(astr)
    print("Your number is: ",astr)
except:
    istr=("0")
    print("Incorrect type: ",istr)
    print("You entered: ",astr,"- not a numer!")


# In[ ]:





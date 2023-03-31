#!/usr/bin/env python
# coding: utf-8

# In[2]:


#1 in the below elements which of them are the values or an expression?eg: values can be string or integer 
#and expression will be mathematicaloperators
#*,'hello',-87.8,-,/,+,6


# In[3]:


print("hello,-87.8,6 are values")


# In[4]:


print("*,-,/,+ are expression")


# In[5]:


#2) WHAT IS DIFFERENCE BETWEEN STRING AND VARIABLE


# In[6]:


print("""strings are combination of sequence of characters and variables are store different type of value
and it contain adress in memory""")


# In[11]:


#3)describe three different data type
print("int is a data type which store integer values")
a = 10
type(a)


# In[12]:


print("float is a another data type in the python and which stores the decimal values")
b=12.9
type(b)


# In[16]:


print("bool is a boolean datatype which tells the condition or number or string is true or false")
a = 10
bool(a)


# #4)What is an expression made up of? What do all expressions do?

# In[17]:


print("expression is made up of combination of operands or operators")
c=23
d=45
#for example
print(c+d-5)


# In[18]:


print("all expressions performs mathematical operation if a sytax of the expression is true")


# In[19]:


#5.) This assignment statements, like spam = 10. What is the difference between an
#expression and a statement?


# In[20]:


print("expression perform calculations it contains values and operators while in statements varible assign a value")


# In[21]:


#6) After running the following code, what does the variable bacon contain?
#bacon = 22
#bacon + 1


# In[22]:


bacon = 22
bacon + 1


# In[23]:


print(bacon)


# In[24]:


print("varible bacon value did not change after running these code")


# In[25]:


#7. What should the values of the following two terms be?
#spam + spamspam;
# spam* 3

print("spam"+"spamspam")


# In[30]:


"spam"*3


# In[28]:


#8) Why is eggs a valid variable name while 100 is invalid?


# In[31]:


print("a variable is contain letters and it also contain numbers and its must st")
print("a variable strats with alphabetic characters")
print("compiler consider 100  as the value")


# In[32]:


#9. What three functions can be used to get the integer, floating-point number, or string
#version of a value?
a =90
int(a)


# In[33]:


type(a)


# In[34]:


float(a)


# In[35]:


type(a)


# In[37]:


str(a)


# In[38]:


type(a)


# In[39]:


print("the three functions used are int(),float() and str()")


# In[41]:


#10)Why does this expression cause an error? How can you fix it?
# 'I have eaten' + 99 + 'burritos';
print("concatenating the string to the integer gives the error")
#we can fix it by changing the INTEGER to the STRING VALUE.
'i have eaten' + '99' + 'burritos'


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# # CONDITIONAL_STATEMENTS

# ## KEYWORDS :
# ### 1. IF
# ### 2. ELSE
# ### 3. ELIF---> ELSE IF (TO CHECK MULTIPLE CONDITIONS)
# 
# ## BLOCKS :
# ### 1. IF BLOCK
# ### 2. IF ELSE BLOCK
# ### 3. NESTED IF ELSE BLOCK
# ### 4. IF ELIF BLOCK
# ### 5. IF ELIF ELSE BLOCK
# 

# # SYNTAX
# # if condition : 
#         # body of if
#         
# # elif condition:
#         # body of elif
#         
# # else condition:
#         # body of else

# In[3]:


#if block

a = int(input("Enter a number---: "))

if a%2==0:
    print("You have entered an even number")
print("Further Code")


# In[4]:


# else if block

a=int(input("Enter a number : "))
if a%2==0:
    print("You have entered a number")
else:
    print("Better luck next time")
print("we are rockstars")


# In[11]:


# Nested if-else block

a=int(input("Enter a number : "))

# check whether the number user entered id divisible by :
# only 2 and 3
# only 2
# only 3
# neither 2 or 3

if a%2==0:
    if a%3==0:
        print(a,'is divisible by both 2 and 3')
    else:
        print(a,'is divisible by only 2')
else:
    if a%3==0:
        print(a,'is divisible by only 3')
    else:
        print(a,'is divisible by neither 2 nor 3')


# In[12]:


a = int(input("Enter the value of A : "))
b = int(input("Enter the value of B : "))
c = int(input("Enter the value of C : "))
if a > b and a > c:
    print(a,"i.e, A is the greatest number.")
elif b > a and b > c:
    print(b,"i.e, B is the greatest number.")
else:
    print(c,"i.e, C is the greatest number.")


# In[ ]:





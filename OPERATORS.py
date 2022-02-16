#!/usr/bin/env python
# coding: utf-8

# # OPERATORS

# # 1. ARITHEMATIC OPERATORS

# In[40]:


# "+","-","*","/","%","//","**"


# In[41]:


a=52
b=47
c=a+b
print(c)
print(type(c))


# In[42]:


print(4+5) #Here, "+" is considered as an operator which perform addition.


# In[43]:


print(5%2) #Here, "%" is the modulus operator which returns the remainder.


# In[44]:


print(7//2) #Here, "//" is the floor division operator.
print(7/2)
print(7%2)


# In[45]:


print(2**4) #Here, "**" is the exponent.
print(5**5)


# # 2. ASSIGNMENT OPERATOR

# In[46]:


# "+=","-=","*=","/=","==","**=","%="


# In[47]:


a=5
print(a)
a+=3
print(a)
a-=2
print(a)


# In[48]:


a **= 2
print(a)


# In[49]:


a%=6
print(a)


# # 3. COMPARISON OPERATOR

# In[50]:


# COMPARISON---- RETURNS TRUE OR FALSE
# ==,!=,>,<,>=,<=


# In[51]:


a=5
b=5
c=10

print(c == a+b)
print(a >=c)


# # 4. LOGICAL OPERATOR

# In[52]:


# "and","or","not"


# In[53]:


a=10
b=20
c=30
d=40

print(a+b == c and c>d)
print(a+b == c and d<c)
print(not(a+b == c or c>d))


# # MUTABLE AND IMMUTABLE

# In[54]:


#A mutable object is one whose value may change in place,
#whereas in an immutable variables change of value will not happen in place.
#Modifying in an immutable variables will rebuild the same variables.


# # 5. IDENTITY OPERATOR

# In[55]:


# "is", "is not"


# In[56]:


a=5
b=5
print(a==b)
print(a is b)
print(a is not b)


# In[57]:


c = 63
d = 36
print(c is not d)


# # MEMBERSHIP OPERATOR

# In[58]:


# "in","not in"


# In[59]:


a="PYTHON"
print('p' in a) #python is case sensitive
print('P' in a)
print('ON' not in a)


# # DATATYPES

# # 1. NUMBERS

# # INT, FLOAT, COMPLEX

# In[60]:


a= 4 #--------INTEGER
print(a)
print(type(a))


# In[61]:


b=5.2 #--------FLOAT
print(b)
print(type(b))


# In[62]:


c=2+3j #----------COMPLEX
print(c)
print(type(c))


# In[63]:


# Indentation error can occur when the spaces or tabes are not placed properly.


# # 2. String

# In[64]:


a = "python"
print(a)
print(type(a))


# In[65]:


# Multi line strings


# In[66]:


b='''Python 
is a 
programming language'''
print(b)


# # * Denoted by ''' '''," ",' '
# # * Concatenation
# # * Indexing
# # * Slicing
# # * Methods

# In[67]:


# "\n" is line break character and
# "\t" is used for giving a tab space in between

a = 'HEY!\nI\nAm\nPython'
print(a)
b = 'HEY!\tI\tAm\tPython'
print(b)


# In[68]:


#CONCATENATION

a='HELLO'
b='STUDENTS'
print(a +' '+b)


# # INDEXING
Indexing starts at 0, so the string hello:

character : h  e  l  l  o
index:      0  1  2  3  4

You can use square brackets to grab single character

character        :  h   e   l   l   o
reverse indexing : -5  -4  -3  -2  -1 
# In[69]:


a= "PYTHON"
print(a[1])
print(a[5])
print(a[-1])
print(a[-4])


# # SLICING

# # SYNTAX

# ### [Start : Stop : Step]
# ### step is default 1
# ### if no start is given and step is +ve the start is 0
# ### if no start is given and step is -ve the start is -1

# In[70]:


alpha = 'abcdef'
alpha[0:3]


# In[71]:


dear =  "KUNAL"
dear[1:5]


# In[72]:


student = "ABHISHEK"
student[2:8:2]


# In[73]:


place = "ghaziabad"
place[1:-5:-1]


# In[74]:


place = "ghaziabad"
place[-5:-1]


# In[75]:


place = "bhopal hapur"
place[0::2]


# In[76]:


place = "manipur mojpur" # spaces are also treated as characters.
place[0::2]


# In[77]:


a="HELLO WORLD"
print(a[6:])
print(a[1:9:2])


# ## if we don't give any stop and step is positive the the entire string is sliced from start to end in direction of left to right
# ## if we don't give any stop and step is negative then the entire string is sliced from start to end in direction of right to left

# In[78]:


a= "PYTHON"
print(a[::-1])
print(a[:])


# # METHODS

# In[79]:


dir(str)


# In[80]:


a = "PYTHON"
print(a)
c= a.lower()
print(c,a)


# In[81]:


a= "hello world"
print(a.capitalize())
print(a.title())


# In[82]:


a= 'ABC'
print(a.center(20,'+'))


# In[83]:


a= ' I AM PYTHON DEVELOPER '
print(a.center(30,'*'))


# In[84]:


# THERE ARE VARIOUS CHECK METHODS WHICH APPLY TO A STRING
# to check for some condition

a= 'python123'
print(a.islower())
print(a.isupper())
print(a.isalpha())
print(a.isalnum())
print(a.isdigit())
print(a.startswith('py'))
print(a.endswith('n'))


# In[85]:


a= 'ARGENTINA'
print(a)
b=a[::-1]
print(b)
b= b.replace('A','$',1)
print(b)
b=b[::-1]
print(b)


# In[86]:


help(str.strip)


# In[87]:


a= '    THIS IS AN EXAMPLE   '
print(a,type(a))
b= a.strip()
print(b)


# In[93]:


a = 'HELLO WORLD'
print(a.count('L'))
print(a.index('WORLD'))
print(a.find('L'))


# In[95]:


help(str.find)


# # LIST

# In[97]:


a=[]
print(a,type(a),len(a))


# In[98]:


# Homogeneous data-------> same type

a = [10,20,30,40]
print(a)


# Heterogeneous data-------> multiple types

b=["hello",2.3,36,[1,2,3]]
print(b)


# In[100]:


# CONCATENATION

A = [1,2,3]
B = [4,5,6]
print(A,B,id(A)) # id displays the actual memory address where the value is stored
C=A+B
print(C)


# # INDEXING AND SLICING

# ### It works the same way it worked on string.

# In[103]:


a= [[10,20],["hello","python"],["hi","i"]]
print(a,len(a))
print(a[0])
print(a[1])
print(a[2])


# In[105]:


help(list.pop)


# In[110]:


a=[10,20,30]
print(a,type(a))
 # APPEND METHOD ADD ITEMS TO END OF THE LIST
b = a.append(40)
print(a,b)
a.append([1,2,3])
print(a)
 # INSERT METHOD ADD ITEM TO THE INDEX POSITION MENTIONED.
a.insert(1,40)
print(a)

#REMOVE METHOD DELETES THE VALUES PASSED AS AN ARGUMENT
#IF VALUE DOES NOT EXIST, AN ERROR IS DISPLAYED

a.remove(40)
print(a)

# POP METHOD REMOVES THE ITEM AT PARTICULAR INDEX,
# BY DEFAULT LAST

b=a.pop()
print(b)
b=a.pop(1)
print(b)


# In[115]:


dir(list)


# In[1]:


# reverse

a=[25,28,15,13,8,6]
print(a,id(a))
a.reverse()
print(a,id(a))


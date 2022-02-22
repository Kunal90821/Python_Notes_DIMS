#!/usr/bin/env python
# coding: utf-8

# # SET & DICTIONARY

# ## SET(MUTABLE)
# 
# #Denoted by {} and items are separated using a,
# 
# #No indexing, no order
# 
# #No duplicates i.e., only unique items
# 
# #Only mutable objects are allowed
# 
# #No Slicing
# 
# #a = set()-----------------> EMPTY SET, if we using curly then it represents empty  dictionary

# In[1]:


a = set()
print(a,type(a),len(a))


# In[2]:


a={1,2,3,4,5}
print(a,type(a),len(a))


# In[3]:


# a = {}
# print(type(a))


# In[7]:


a={1.23,3,"hello",(10,20,30)}
print(a,type(a),len(a))


# In[5]:


s={1,1,1,2,2,2,3,3,3}
print(s)
# s[1]  ,it will given an error because set doesn't support indexing.


# In[6]:


a = 'PYTHON'
print(a,type(a))
b=list(a)
print(b,type(b))
s=set(a)
print(s,type(s))


# In[8]:


a = "HELLO"
b = list(a)
c = set(a)
print(len(b)==len(c))
print(b)
print(c)


# In[9]:


dir(set)


# In[10]:


s=set()
print(s,id(s)) # id denotes address


# In[11]:


s.add(10)
print(s)


# In[12]:


s.add("Hello")
print(s)


# In[13]:


s.add((1,2,3))
print(s)


# In[14]:


s.remove("Hello")
print(s)


# In[17]:


s.discard((1,2,3,4)) #-- removes element, no error if element does not exist
print(s)


# In[22]:


s1  = {1,2,3,4,5}
s2  = {4,5,6}

#UNION

print(s1.union(s2))
print(s1 | s2)

#INTERSECTION

print(s1.intersection(s2))
print(s1 & s2)

#DIFFERENCE

print(s1.difference(s2))
print(s1 - s2)

#SYMMETRIC DIFFRENCE

print(s1.symmetric_difference(s2))
print((s1-s2)|(s2-s1))
print(s1^s2)


# # ITERATING A SET

# In[1]:


s = {"MATHS","ENGLISH","SCIENCE"}
for i in s:
    print(i)


# # DICTIONARY(MUTABLE)

# Denoted by {key:value,.....} and items are separated using a,
# 
# No indexing, no slicing, no order (unordered)
# 
# Values can be accessed by using key as index
# 
# Keys : "Unique across the dictionary" Immutable objects
#     
# Example : d={'a':2,'b':3}=====> d['a']-->2
#     
# d=[]--> Empty Dict.

# In[3]:


d = {}
print(d,type(d),len(d))


# In[7]:


d = {'a':1,'b':2}
print(d,len(d))
print(d['a'])
print(d['b'])
# print(d['c'])    -----------error


# In[8]:


d = {2:'c','a':1,'b':2}
print(d,len(d))
print(d[2])


# In[29]:


d = {}
print(d)


# In[30]:


dir(dict)


# In[38]:


a=100
b=200
c=300
d={'m':a,'n':b,'p':c}
print(d['m'])
print(d['n'])
print(d['p'])
print(d,type(d))


# In[39]:


d["name"]="KUNAL"
print(d,type(d))


# In[40]:


d['p']+=100
print(d)


# In[31]:


help(dict)


# # DICTIONARY METHODS
# 
# - Keys
#     
# - Values
#     
# - Items

# In[41]:


d = {'PYTHON':200,'JAVA':250,'PHP':150}
print(d)
print(d.keys())
print(d.values())
print(d.items())


# # Forming a dictionary using two list without using zip function

# In[44]:


a = ['PYTHON','JAVA','PHP']
b = [100,200,300]
for i in range (len(a)):
    di={a[i]:b[i]}
    print(di)

di={a[i]:b[i] for i in range (len(a))}
print(di)


# In[45]:


# another way
a = ['PYTHON','JAVA','PHP']
b = [100,200,300]
c = []
n = min(len(a),len(b))
for i in range(n):
    c.append((a[i],b[i]))
print(c)
d = dict(c)
print(d)


# In[57]:


a = ['PYTHON','JAVA','PHP']
b = [100,200,300]
c = list(zip(a,b))
print(c)
d = dict(c)
print(d)


# # Count the number of occurence of each character in a given string

# In[28]:


a = 'ababababababa'
i = a.count("a")
j = a.count("b")
d = {'a' : i,'b' : j}
print(d)

# Another way

di = {}
for i in a:
    if i not in di:
        di[i] = a.count(i)
print(di)

# Another way

a = "abababbabababa"
x = 0
y = 0
for i in a:
    if(i == 'a'):
        x+=1
    elif(i == 'b'):
        y+=1
print('a:',x,'b:',y)


# # Ques1: Create a dictionary with sqr of number as values and numb key

# # Ques2: Concatenate two dict.

# In[7]:


# Answer 1

x=int(input("Enter range : "))
di={}
for i in range(1,x+1):
    di[i]=i*i
print(di)


# In[25]:


# Answer 2

d1={'PYTHON':100,'JAVA':150,'C':200}
d2={'PHP':200,'C++':300}
print(d1)
print(d2)
d1.update(d2)
print(d1)


# In[ ]:





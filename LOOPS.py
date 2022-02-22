#!/usr/bin/env python
# coding: utf-8

# # WHILE--- When we don't know the number of times we want to run the loop
# # FOR---- When we know the number of times we want to run the loop
# # while loop
# # syntax
# # while condition : 
#         # body of the loop

# In[ ]:


a=1
while a<=10:
    print(a)
    a+=1    #a = a+1


# In[ ]:


print(10,20,30)
print(10,20,30, sep="-->") #sep keyword is used to separate the values with the given/desired separator, default seaparator is space.


# In[ ]:


help(print)


# In[ ]:


a=1
while a<=10:
    print(a,end=' ')
    a+=1
print()
print("outside loop")


# In[ ]:


first ="Kunal"
last ="Kumar"

print('Hi',first,last,'How are you?')
print('Hi {} {} How are you?'.format(first,last))


# In[ ]:


a=5
b=6
print(a, "*",b, '=',a*b)
print('{} * {} = {}'.format(a,b,a*b))


# In[ ]:


x=int(input("Enter any number "))
i=1
while i<=10:
    print('{} * {} = {}'.format(x,i,x*i))
    i+=1


# In[ ]:


a=2
b=3
c=4
i=1
while i<=10:
    print(a,'*',i, "=" ,a*i,'         ',b, '*' ,i, "=", b*i,'        ',c, '*',i, "=", c*i)
    i+=1


# In[ ]:


x=int(input("Enter a number : "))
y=int(input("Enter another number : "))
print()
while x<=y:
    i=1
    while i<=10:
        print('{} * {} = {}'.format(x,i,x*i))
        i+=1
    print()
    x+=1


# In[ ]:


x=int(input("Enter a number : "))
y=int(input("Enter another number : "))
i=1
print()
while i<=10:
    while x<=y:
        print('{} * {} = {}'.format(x,i,x*i),end="\t")
        x+=1
        i+=1
    print()


# # WAP to print fibonaaci series from 0 to 100

# In[ ]:


a=0
b=1
while b<=100:
    c=a+b
    print('{}'.format(c),end="\t")
    a=b
    b=c


# # For Loop
# # Syntax
# # for variable in sequence:
#         # Body of the loop

# In[ ]:


for i in [10,20,30]:
    print(i)


# In[ ]:


for j in "KUNAL KUMAR":
    print(j)


# # Range Function :
# ## Syntax
# 
# range(start,stop,step)
#  
#     *Step is default 1
#     
#     *Start is default 0
#     
#     *Stop is mandatory and is not included in the range

# In[ ]:


for i in range(5):
    print(i)


# ## Print first ten terms of fibonaaci series using range--

# In[1]:


a=0
b=1
for i in range(10):
    c=a+b
    print(c,end="\n")
    a=b
    b=c
    


# ## Print factorial using range :

# In[6]:


num = int(input("Enter any number : "))
x=1
for i in range(1,num+1):
    x=x*i
print("Factorial of ",num," is ",x)


# ## Pattern of any word

# In[10]:


a=input("Enter any word : ")
b=''
for i in a:
    b = b+i
    print(b)


# ## TASK:
# #### Given a string find out the largest word (containing only alphabets) in the string.

# In[11]:


help(max)


# In[13]:


a = input("Enter the sentence: ")
long = max(a.split(), key = len)
print('Longest Word is: ',long)
print(len(a))


# In[14]:


# Print the armstrong number.

n = int(input("Enter the number: "))
sum = 0
temp = n
while temp > 0: # Here, temp holds the value entered by user.
    digit = temp % 10 # Here, we get the remainder of the number entered, 1st.
    sum = sum + (digit ** 3) # Here, '**' is used for printing the power of a particular number, 3rd.
    temp = temp // 10 # Here, we got the quotient of the number, 2nd.
if n == sum:
    print(n, 'is an armstrong number.')
else:
    print(n, 'is not an armstrong number.')


# In[17]:


# print the reverse number with & without using loop.

#With loop:-
n = int(input("Enter the number: "))
rev = 0
while n!=0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10
print(rev)


# In[16]:


# Without loop
m = int(input("Enter the number: "))
b = int(str(m)[::-1])
print(b)


#!/usr/bin/env python
# coding: utf-8

# In[1]:


kilometers = float(input("Enter value in kilometers: "))

# conversion factor
conversion = 0.621371

# calculate miles
miles = kilometers * conversion
print(kilometers,miles)


# In[3]:


# change this value for a different result
celsius = float(input("Enter value in celsius: "))

# calculate fahrenheit
fahrenheit = (celsius * 1.8) + 32
print((celsius,fahrenheit))


# In[6]:



import calendar
yy = int(input("Enter year: "))
mm = int(input("Enter month: "))

# display the calendar
print(calendar.month(yy, mm))


# In[12]:


import cmath

a = 25
b = 63
c = 10

# calculate the discriminant
d = (b**2) - (4*a*c)

# find two solutions
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print(sol1,sol2)


# In[14]:


x = 100
y = 58
# code to swap 'x' and 'y'
x, y = y, x
print ("After swapping: ")
print("Value of x : ", x, " and y : ", y)


# In[ ]:





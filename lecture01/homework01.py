#!/usr/bin/env python
# coding: utf-8

# In[4]:


import math
a= int(input ("Введите длину первой стороны "))
print ("a= ", a)
b= int(input ("Введите длину второй стороны "))
print ("b= ", b)
x= int(input ("Введите величину угла между ними "))
print ("x= ", x)
c= math.sqrt (math.pow(a,2)+ math.pow(b,2)-2*a*b*math.cos(math.radians(x)))
print ("c= ",c)


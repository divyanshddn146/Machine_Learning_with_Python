# -*- coding: utf-8 -*-
"""Untitled15.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1apvBYBoFA1BIel77UBxoAptEiJjF17cT
"""

str1 = "HELLOWRLD"
list1 = []
for i in str1:
    list1.append(i)
k = 16
m = 0
for i in range(len(list1)):
    if(i%2==0):
        print(m*" "+list1[i],end=(k*" "))
        k=k-4
        m = m+2
    else:
        print(list1[i])
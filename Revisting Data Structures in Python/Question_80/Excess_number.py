# -*- coding: utf-8 -*-
"""Untitled15.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1apvBYBoFA1BIel77UBxoAptEiJjF17cT
"""

n = int(input("Enter the value of n:"))
print("Enter the values for list:")
list1 = []
c = 0
while(c!=n):
    x = int(input())
    if(x>100):
        list1.append("EXCESS")
    else:
        list1.append(x)
    c = c + 1

print(list1)
# -*- coding: utf-8 -*-
"""Untitled15.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1apvBYBoFA1BIel77UBxoAptEiJjF17cT
"""

n = int(input("Enter the value of n:"))
i = 2
j = 9
list1 = []
for k in range(n):
    list1.append(f'{i}/{j} ')
    i = i*2
    j = j+4
new = ""
for i in range(n):
    new = new + list1[i]
new = new.strip()
new = new.replace(" ",",")
print(new)
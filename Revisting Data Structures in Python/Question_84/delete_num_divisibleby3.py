# -*- coding: utf-8 -*-
"""Untitled15.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1apvBYBoFA1BIel77UBxoAptEiJjF17cT
"""

list1 = []
for i in range(1,21):
    list1.append(i)
print(list1)
for i in list1:
    if(i%3==0):
        list1.remove(i)
print(list1)
# -*- coding: utf-8 -*-
"""Untitled14.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tQHoX16w_jmxRRFfL1rpzUHomhb_SPK1
"""

text = ("Line 1\nLine 2 3\nLine 3")

d = 0
u = 0
l = 0
s = 0
for i in text:
    if(i.isdigit()):
        d = d + 1
    elif(i.isupper()):
        u = u + 1
    elif(i.islower()):
        l = l + 1
    elif(i.isalnum() == False):
        s = s + 1

print(f"Text has {d} digits , {u} uppercase letters , {l} lowercase letters and {s} special characters")
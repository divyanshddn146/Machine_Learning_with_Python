# -*- coding: utf-8 -*-
"""Untitled14.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tQHoX16w_jmxRRFfL1rpzUHomhb_SPK1
"""

def new_num(n,w):
    n = str(n)
    if(w<len(n)):
        return n
    else:
        c = w - len(n)
        new = "" + n
        for i in range(c):
            new = new + "*"
        return new


user_input = int(input("Enter a floating point number:"))
width = int(input("Enter the width:"))
result = new_num(user_input,width)
print(result)
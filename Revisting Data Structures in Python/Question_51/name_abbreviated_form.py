# -*- coding: utf-8 -*-
"""Untitled14.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tQHoX16w_jmxRRFfL1rpzUHomhb_SPK1
"""

name = input("Enter your name:")
list_name = name.split()
new = ""
for i in range(len(list_name)):
    if(i==((len(list_name))-1)):
        new = new + list_name[i].capitalize()
    else:
        new = new + list_name[i][0].upper() + "."

print(new)
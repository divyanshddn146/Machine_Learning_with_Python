# -*- coding: utf-8 -*-
"""Untitled14.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tQHoX16w_jmxRRFfL1rpzUHomhb_SPK1
"""

def new_string(s):
    new = s.replace("\n","")
    return new

s1 = """ hi this is divyansh \n it is a wonderful day \n thanks"""
result = new_string(s1)
print(result)
# -*- coding: utf-8 -*-
"""Untitled14.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tQHoX16w_jmxRRFfL1rpzUHomhb_SPK1
"""

def remove_spaces(input_string):
    result = input_string.strip()
    return result

user_input = input("Enter a string with leading and trailing spaces: ")
result = remove_spaces(user_input)
print(result)
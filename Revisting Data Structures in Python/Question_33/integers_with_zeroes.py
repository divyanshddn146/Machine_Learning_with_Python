# -*- coding: utf-8 -*-
"""Untitled14.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tQHoX16w_jmxRRFfL1rpzUHomhb_SPK1
"""

def format_int_with_zeros(number, width):
    formatted_number = str(number).zfill(width)
    return formatted_number


input_number = 42
specified_width = 5
result = format_int_with_zeros(input_number, specified_width)
print(result)
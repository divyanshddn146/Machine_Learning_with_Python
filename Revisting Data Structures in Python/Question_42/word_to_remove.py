# -*- coding: utf-8 -*-
"""Untitled14.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tQHoX16w_jmxRRFfL1rpzUHomhb_SPK1
"""

def remove_word(input_string, word_to_remove):
    list1 = input_string.split()
    new = ""
    for i in list1:
        if(i==word_to_remove):
            continue
        new = new + i + " "
    return new.strip()

# Example usage:
user_input = input("Enter a string: ")
word_to_remove = input("Enter the character to remove: ")
result = remove_word(user_input, word_to_remove)
print(result)
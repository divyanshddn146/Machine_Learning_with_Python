# -*- coding: utf-8 -*-
"""Untitled8.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_Mu7mK4-bQJwqTMNuis9LcLBIfMc1qfi
"""

current_date = input("Enter current date:")
current_date_list = current_date.split("/")
dob = input("Enter your date of birth:")
dob_list = dob.split("/")
current_date_list = [int(i) for i in current_date_list]
dob_list = [int(i) for i in dob_list]
if current_date_list[1] < dob_list[1] or (current_date_list[1] == dob_list[1] and current_date_list[0] < dob_list[0]):
    age = current_date_list[2] - dob_list[2] - 1
else:
    age = current_date_list[2] - dob_list[2]

print(f"Your age is {age} years.")
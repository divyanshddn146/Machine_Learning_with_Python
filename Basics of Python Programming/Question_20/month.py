# -*- coding: utf-8 -*-
"""Untitled8.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_Mu7mK4-bQJwqTMNuis9LcLBIfMc1qfi
"""

user_input = int(input("Enter any input value from 1 to 12:"))
if(user_input<1 and user_input>12):
    print("Entered value is not in range from 1 to 12")
month_list = ['January','February', 'March', 'April','May','June','July','August','September','October','November','December']
print(f"{user_input} refers to month {month_list[user_input-1]}")
# -*- coding: utf-8 -*-
"""Untitled8.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_Mu7mK4-bQJwqTMNuis9LcLBIfMc1qfi
"""

age = {15:[56,170],16:[60,173],17:[64,175],18:[66,176]}
user_input = int(input("Enter age from 15-18 years:"))
for i,j in age.items():
    if(user_input==i):
        print(f"Age {i} has height {j[0]} and weight as {j[1]}")
    else:
        print("Value not in range")
# -*- coding: utf-8 -*-
"""Untitled8.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_Mu7mK4-bQJwqTMNuis9LcLBIfMc1qfi
"""

user_input = input("Enter your martial status('S' for Separated,'M' for Married,'D' for Divorced,'U' for Unmarried):")
user_input = user_input.lower()
if(user_input == 'm'):
    print("Martial Status is Married")
elif(user_input == 's'):
    print("Martial Status is Seperated")
elif(user_input == 'd'):
    print("Martial Statuis is Divorced")
elif(user_input == 'u'):
    print("Martial Status is Unmarried")
else:
    print("Invalid Value entered")
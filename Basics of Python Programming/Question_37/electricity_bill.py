# -*- coding: utf-8 -*-
"""Untitled8.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_Mu7mK4-bQJwqTMNuis9LcLBIfMc1qfi
"""

user_input = float(input("Enter your consumption unit:"))
if(user_input>=0 and user_input<=150):
    charge = user_input*3
    print(f"You have to pay {charge} for elcticity")
elif(user_input>150 and user_input<=300):
    charge = user_input*3.75+100
    print(f"You have to pay {charge} for elcticity")
elif(user_input>300 and user_input<=450):
    charge = user_input*4 + 250
    print(f"You have to pay {charge} for elcticity")
elif(user_input>450 and user_input<=600):
    charge = user_input*4.25+400
    print(f"You have to pay {charge} for elcticity")
elif(user_input>600):
    charge = 400 + user_input*5
    print(f"You have to pay {charge} for elcticity")
else:
    print("Invlaid value entered")
# -*- coding: utf-8 -*-
"""Untitled8.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_Mu7mK4-bQJwqTMNuis9LcLBIfMc1qfi
"""

for i in range(5):
    print("")
    for j in range(5):
        if(i==j):
            print("$",end = " ")
        elif(j==0 or j ==4 or i == 0 or i==4):
             print("*",end = " ")
        else:
            print(" ",end = " ")


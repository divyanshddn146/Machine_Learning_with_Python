# -*- coding: utf-8 -*-
"""Untitled15.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1apvBYBoFA1BIel77UBxoAptEiJjF17cT
"""

products_prices = {
    "Laptop": 1200.00,
    "Smartphone": 599.99,
    "Headphones": 49.99,
    "Coffee Maker": 89.95,
    "Backpack": 39.99,
}
print('We have products like:')
for product, price in products_prices.items():
    print(f"{product}: ${price}")
dict1 = {}
k = 1
for i,j in products_prices.items():
    dict1[k] = j
    k = k + 1

print("What do you need 1) Laptop 2)Smartphone 3)Headphones 4) Coffe Maker 5) Backpack and q to quit")
sum = 0
while(True):
    user_input = input("")
    if(user_input == 'q' or user_input == 'Q'):
        break
    if(int(user_input)>5 or int(user_input)<0):
        print("Invalid Input")
    sum = sum + dict1[int(user_input)]

print(f"Your total amount is {sum}")
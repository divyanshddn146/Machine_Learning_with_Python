# -*- coding: utf-8 -*-
"""Untitled8.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_Mu7mK4-bQJwqTMNuis9LcLBIfMc1qfi
"""

# Program for bill
more_item = True
total_cost = 0
item_name_list = []
item_quantity_list = []
item_price_list = []
while(more_item):
    item_name = input("Enter the name of item:")
    item_name_list.append(item_name)
    item_quantity = int(input(f"Enter the quantity of item {item_name}:"))
    item_quantity_list.append(item_quantity)
    item_price = float(input(f"Enter the price per unit of item {item_name}:"))
    item_price_list.append(item_price*item_quantity)
    total_cost = total_cost + item_price*item_quantity
    user_input = input("Do you want to add more items(Y/N):")
    if(user_input == "N" or user_input == "n"):
        more_item = False
    else:
        more_item = True

print("********BILL********")
for i in range(len(item_name_list)):
    print(f"{item_name_list[i]}\t{item_quantity_list[i]}\t{item_price_list[i]}")
print("**********************")
print(f"Total Amount to be paid is {total_cost}")
print("**********************")
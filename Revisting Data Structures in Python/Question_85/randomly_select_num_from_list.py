# -*- coding: utf-8 -*-
"""Untitled15.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1apvBYBoFA1BIel77UBxoAptEiJjF17cT
"""

import random

def random_select_item(input_list):
    if not input_list:
        return None
    else:
        return random.choice(input_list)


my_list = ["apple", "banana", "orange", "grape", "kiwi"]

selected_item = random_select_item(my_list)

if selected_item is not None:
    print("Randomly selected item:", selected_item)
else:
    print("The list is empty.")
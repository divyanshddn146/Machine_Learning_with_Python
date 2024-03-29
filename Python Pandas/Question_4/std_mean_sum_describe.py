# -*- coding: utf-8 -*-
"""Untitled

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JttHq2PyT9G8yq5Bbhsd3_zndaSr3osP
"""

import pandas as pd
import numpy as np

data = {
    'Name': ['John', 'Alice', 'Bob', 'Eva'],
    'Age': [25, 30, 35, 28],
    'Rating': [4.5, 3.8, 4.2, 5.0]
}

df = pd.DataFrame(data)

print("To find sum of columns")

print(df.iloc[:,1:].sum())
print("")
print("To find average age and rating\n")

print(df.iloc[:,1:].mean())
print("")
print("To find standard deviation")

print(df.iloc[:,1:].std())
print("")
print("To describe dataframe")

print(df.describe())
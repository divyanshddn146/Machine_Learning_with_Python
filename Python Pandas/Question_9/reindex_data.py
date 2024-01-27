# -*- coding: utf-8 -*-
"""Untitled

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JttHq2PyT9G8yq5Bbhsd3_zndaSr3osP
"""

import pandas as pd

import pandas as pd
import numpy as np

# Create a DataFrame with any values, including empty or missing values
data = {
    'Name': ['Alice', 'Bob', 'Charlie', np.nan, 'Eva'],
    'Age': [25, 30, np.nan, 28, 35],
    'Salary': [50000, np.nan, 60000, 75000, 80000],
    'City': ['New York', 'San Francisco', np.nan, 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)

print(df)
print("\n")
print(df.reindex([3,1,5,4,2],axis=0).fillna(value=100))
print("\n")
print(df.reindex(["Salary","City","Name","Salary"],axis=1).fillna(value=25))
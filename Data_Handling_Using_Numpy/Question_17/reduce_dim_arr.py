# -*- coding: utf-8 -*-
"""Untitled18.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZQamPoJ7CjFYrumHYNvOyl4hCQ-RM-_A
"""

import numpy as np

np_arr = np.random.randint(low=0, high=100, size=(1,3,3))
print(np_arr)
reduced_dim_arr = np_arr.squeeze()
print(reduced_dim_arr)


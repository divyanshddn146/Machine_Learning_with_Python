# -*- coding: utf-8 -*-
"""Untitled18.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZQamPoJ7CjFYrumHYNvOyl4hCQ-RM-_A
"""

import numpy as np

np_arr = np.random.randint(low=0, high=100, size=(12))
new_arr = np_arr.reshape((4,3))
print(new_arr)


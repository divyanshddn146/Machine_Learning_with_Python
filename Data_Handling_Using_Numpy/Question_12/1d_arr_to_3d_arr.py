# -*- coding: utf-8 -*-
"""Untitled18.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZQamPoJ7CjFYrumHYNvOyl4hCQ-RM-_A
"""

import numpy as np

list1 = [[[1,2,3],[4,5,6],[7,8,9]],[[2,3,4],[6,7,8],[3,6,9]],[[1,4,7],[5,7,9],[2,6,8]]]
np_arr = np.array(list1)
flatten_arr = np_arr.flatten()
print(flatten_arr)
arr_3d = flatten_arr.reshape((3,3,3))
print(arr_3d)

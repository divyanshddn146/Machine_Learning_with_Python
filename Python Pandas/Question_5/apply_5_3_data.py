# -*- coding: utf-8 -*-
"""Untitled

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JttHq2PyT9G8yq5Bbhsd3_zndaSr3osP
"""

import pandas as pd
import numpy as np


df = pd.DataFrame(np.random.random(size=(5,3)))
print(df)
print(df.apply(np.sum,axis=1))
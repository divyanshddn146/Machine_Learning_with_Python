# -*- coding: utf-8 -*-
"""Untitled8.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_Mu7mK4-bQJwqTMNuis9LcLBIfMc1qfi
"""

import math

angle = float(input("Enter angle:"))

sin_value = math.sin((angle*math.pi)/180)
cos_value = math.cos((angle*math.pi)/180)
tan_value = math.tan((angle*math.pi)/180)
if(angle==0 or angle%90==0):
    print(f"{angle} does not lie in any quadrant")
elif(sin_value>0 and cos_value>0 and tan_value>0):
    print(f"{angle} lies in first quadrant")
elif(sin_value>0 and cos_value<0 and tan_value<0):
    print(f"{angle} lies in second quadrant")
elif(sin_value<0 and cos_value<0 and tan_value>0):
    print(f"{angle} lies in third quadrant")
elif(sin_value<0 and cos_value>0 and tan_value<0):
    print(f"{angle} lies in fourth quadrant")
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 12:26:29 2021

@author: sjcet
"""

#8. Demonstrate the use of insert() function in 1D and 2D array.

import numpy as np

array_1d=np.array([1,2,3,4,5])
array_2d=np.arange(12).reshape(3, 4)

print("1D array")
print(array_1d)
print("\nthe use of insert() function in 1D array")
x=np.insert(array_1d,2,6)
print(x)

print("\n2D array")
print(array_2d)
print("\nthe use of insert() function in 2D array")
y=np.insert(array_2d, 1,9, axis=1)
print(y)
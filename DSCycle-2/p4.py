#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 10:25:35 2021

@author: sjcet
"""

#4. Create an one dimensional array using arange function containing 10 elements.
#Display
#a. First 4 elements
#b. Last 6 elements
#c. Elements from index 2 to 7

import numpy as np

array_1d=np.array([1,2,3,4,5,6,7,8,9,10])
print("First 4 elements ",array_1d[:4])
print("Last 6 elements ",array_1d[4:])
print("Elements from index 2 to 7 ",array_1d[2:7])
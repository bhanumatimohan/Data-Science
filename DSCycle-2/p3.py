#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 12:21:57 2021

@author: sjcet
"""

#3. Familiarize with the functions to create
#a) an uninitialized array
#b) array with all elements as 1,
#c) all elements as 0

import numpy as np

print("an uninitialized array :")
print(np.empty([2,2]))
print("array with all elements as 1 :")
print(np.full([2,2],1))
print("all elements as 0 :")
print(np.zeros([2,2]))
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 10:49:15 2022

@author: sjcet
"""

import numpy as np

matrix_1=np.array([[1,2],[3,4]])
matrix_2=np.array([[5,6],[7,8]])

print("Matrix 1")
print(matrix_1)
print("Matrix 2")
print(matrix_2)

print("Transpose of Matrix 1")
print(matrix_1.transpose())
print("Transpose of Matrix 2")
print(matrix_2.transpose())

print("Matrix Multiplication")
print(np.dot(matrix_1,matrix_2))
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 11:37:25 2021

@author: sjcet
"""

#4. Given 3 Matrices A, B and C. Write a program to perform matrix multiplication of the 3 matrices.

import numpy as np

A=np.matrix("1 2 ; 3 4")
print("Matrix A\n ",A)
B=np.matrix("5 6 ; 7 8")
print("Matrix B\n ",B)
C=np.matrix("9 10 ; 11 12")
print("Matrix C\n ",C)

result=np.dot(A,B)

matrix=np.dot(result,C)
print("Products of 3 matrices is: \n",matrix)

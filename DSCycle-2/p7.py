#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 12:06:24 2021

@author: sjcet
"""

#7.Create two 2D arrays using array object and

#a. Add the 2 matrices and print it
#b. Subtract 2 matrices
#c. Multiply the individual elements of matrix
#d. Divide the elements of the matrices
#e. Perform matrix multiplication
#f. Display transpose of the matrix
#g. Sum of diagonal elements of a matrix

import numpy as np

x=np.array([[1,2],[3,4]])
y=np.array([[5,6],[7,8]])

print("Add the 2 matrices")
print(np.add(x,y))
print("Subtract 2 matrices")
print(np.subtract(x,y))
print("Multiply the individual elements of matrix")
print(np.multiply(x,y))
print("Divide the elements of the matrices")
print(np.divide(x,y))
print("Perform matrix multiplication")
print(np.dot(x,y))
print("Display transpose of the matrix")
print(x.transpose())
print(y.transpose())
print("Sum of diagonal elements of a matrix")
print(np.trace(x))
print(np.trace(y))
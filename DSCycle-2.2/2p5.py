#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 11:45:56 2021

@author: sjcet
"""

import numpy as np;

matrix=np.random.randint(0,20,9).reshape(3,3)
print("Matrix x: \n", matrix)
y=matrix.transpose();
print("Transpose of x :\n ",y)

skew=np.multiply(y,-1);
print("negative of transpose :\n ",skew)
if matrix.all() == y.all():
    print("Matrix is symmetric")
else:
    print("Matrix is not symmetric")
if matrix.all() == ~y.all():
    print("Matrix is skew symmetric")
else:
    print("Matrix is not skew matrix")
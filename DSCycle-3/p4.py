#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 12:27:19 2021

@author: sjcet
"""

#4. Display the above data using multiline plot( 3 different lines in same graph)
# Display the description of the graph in upper right corner(use legend())
# Use different colors and line styles for 3 different lines

import matplotlib.pyplot as plt
import numpy as np

x = [1,2,3,4,5]
y = [3,3,3,3,3]
z = [4,4,4,4,4]


plt.plot(x, y, label='line 1')
plt.plot(y, x, label='line 2')
plt.plot(z, x, label='line 3')
plt.legend()
plt.show()
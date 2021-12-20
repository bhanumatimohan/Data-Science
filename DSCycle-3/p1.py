#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 12:11:20 2021

@author: sjcet
"""

#1. Sarah bought a new car in 2001 for $24,000. The dollar value of her car changed each year as shown in the table below.
#Value of Sarah&#39;s Car
#Year Value
#2001 $24,000
#2002 $22,500
#2003 $19,700
#2004 $17,500
#2005 $14,500
#2006 $10,000
#2007 $10,000
#Represent the following information using a line graph with following style properties
# X- axis - Year
# Y –axis - Car Value
# title –Value Depreciation (left Aligned)
# Line Style dashdot and Line-color should be red
# point using * symbol with green color and size 20
#Subplot() provides multiple plots in one figure.

import matplotlib.pyplot as plt
import numpy as np

#plot 1:
x = np.array([2001,2002,2003,2004,2005,2006,2007])
y= np.array([24000,22500,19700,17500,14500,10000,10000])

print("x-axis=> Year    y-axis=> Car Value")
plt.plot(x,y, ls = '-.',color = 'r',marker= '*', ms='20', mfc='green', mec='green')
plt.title("Value Depreciation", loc='left')
plt.xlabel("Year")
plt.ylabel("Car Value")
plt.show()
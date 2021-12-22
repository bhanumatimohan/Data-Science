#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 11:40:04 2021

@author: sjcet
"""

#3. Create scatter plot for the below data:(use Scatter function) 

#Create scatter plot for each Segment with following properties within one graph
# X Label- Months of Year with font size 18
# Y-Label- Sales of Segments
# Title –Sales Data
# Color for Affordable segment- pink
# Color for Luxury Segment- Yellow
# Color for Super luxury segment-blue

import matplotlib.pyplot as plt
import numpy as np

plt.title('Sales Data')
plt.xlabel('Months of Year')
plt.ylabel('Sale of Food')
x = np.array([173,153,195,147,120,144,148,109,174,130,172,131])
y = np.array([173,153,195,147,120,144,148,109,174,130,172,131])
plt.scatter(x,y, color='hotpink')
x = np.array([185,185,126,134,196,153,112,133,200,145,167,110])
y = np.array([185,185,126,134,196,153,112,133,200,145,167,110])
plt.scatter(x, y, color='yellow')

x = np.array([189,189,105,112,173,109,151,197,174,145,177,161])
y = np.array([189,189,105,112,173,109,151,197,174,145,177,161])
plt.scatter(x, y, color='blue')
plt.show()
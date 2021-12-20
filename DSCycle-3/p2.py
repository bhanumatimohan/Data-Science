#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 11:32:53 2021

@author: sjcet
"""

#2. Use subplot function to draw the line graphs with grids(color as blue and line style dotted) for the above information as 2 separate graphs in two rows
#a) Properties for the Graph 1:

# X label- Days of week
# Y label-Sale of Drinks
# Title-Sales Data1 (right aligned)
# Line –dotted with cyan color
# Points- hexagon shape with color magenta and outline black

#b) Properties for the Graph 2:
# X label- Days of Week
# Y label-Sale of Food
# Title-Sales Data2 ( center aligned)
# Line –dashed with yellow color
# Points- diamond shape with color green and outline red

import matplotlib.pyplot as plt
import numpy as np


x= np.array(['Mon','Tues','Wed','Thurs','Fri'])
y= np.array([300,450,150,400,650])

plt.subplot(1, 2, 1)
plt.title("Sales Data1")
plt.xlabel("Days of Week")
plt.ylabel("Sale of Drinks")

plt.plot(x, y, ':c')
plt.plot(x, y, 'Hm',mec='k')
plt.grid(color="blue", ls=':')


c= np.array(['Mon','Tues','Wed','Thurs','Fri'])
v= np.array([400,500,350,300,500])
plt.subplot(1, 2, 2)
plt.title("Sales Data2")
plt.xlabel("Days of week")
plt.ylabel("Sales of Food")

plt.plot(c,v, '--y')
plt.plot(c,v, 'Dg',mec='r')

plt.grid(color='blue', ls=':')
plt.show()


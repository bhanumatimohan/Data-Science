#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 11:59:50 2021

@author: sjcet
"""

#4. 100 students were asked what their primary mode of transport for getting to school was. The results of this survey are recorded in the table below. Construct a bar graph representing this information.

#Create a bar graph with
# X axis -mode of Transport and Y axis ‘frequency’
# Provide appropriate labels and title
# Width .1, color green

import matplotlib.pyplot as plt
import numpy as np

plt.title('Students transportation')
plt.xlabel('Mode of Transport')
plt.ylabel('Frequency')

x = np.array(['Walking','Cycling','Car','Bus','Train'])
y = np.array([29,15,35,18,3])
plt.bar(x, y, color="#4CAF50",width = 0.1)
plt.show()
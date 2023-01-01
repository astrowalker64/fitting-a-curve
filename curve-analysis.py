#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  1 12:04:04 2023

@author: stuart
"""

import numpy as np
from scipy.stats import linregress
import matplotlib.pyplot as plt

datafile = open("measurements.txt", "r")
data = []
for line in datafile:
    s = line.split()
    ss = [float(x) for x in s]
    data.append(ss)
data = np.array(data)

invI = data[:, 0]
invIerr = data[:, 1]
rad = data[:, 2]
raderr = data[:, 3]

plt.scatter(invI, rad)
plt.xlabel("1/I")
plt.ylabel("radius")
plt.show()



# -*- coding: utf-8 -*-

import numpy as np

a = np.floor( 10*np.random.random((3,4)))
b = np.floor( 10*np.random.random((3,4)))
#print(a)
#print(b)

c= np.vstack((a,b))
print(c)

d = np.hstack((a,b))
print(d)
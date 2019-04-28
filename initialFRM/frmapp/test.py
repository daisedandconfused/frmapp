"""

import math

def matrix():

    be = [[12, 13, 8], [2, 1, 87], [16, 6, 4]]

    return be


b = matrix()

print("b[1][2] =", b[1][2])

def rounded():

    n = 0.3
    y = 0.45

    x = (n+y)*5
    k = math.floor((n+y)*5)

    return x, k

x, k = rounded()

print(x, k)

x = 1
while True:
    print("To infinity and beyond! We're getting close, on %d now!" % (x))
    x += 1
"""
import numpy as np

def function(x):

    vec = np.zeros((x, 4))

    for i in range(1, x):
        vec[i][1] = 3
        vec[i][2] = 7
        vec[i][3] = 0.5

    return vec, vec.shape[0]

v, rows = function(12)


import numpy as np

def previousevent(n):

    p = np.zeros(((2**(n-2)), n-2), dtype=int)
    a = p.shape[0]
    b = p.shape[1]

    # for i in range(0, z, 1):
    #     p[i][n-2] = 2

    # element 4th row, 3rd column:
    p[3][2] = 11
    return p, a, b


p, a, b = previousevent(n=6)

print(p, a, b)

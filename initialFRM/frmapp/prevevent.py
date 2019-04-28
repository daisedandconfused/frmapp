import itertools
import numpy as np

def previousevent(n):

    r = n-2
    p = list(itertools.product([1, 2], repeat=r))
    return p

#    matrix = []

#    while p !=[]:
#        matrix.append(p[:1])
#        p = p[1:]
#    return matrix

# v = previousevent(4)


# y = v[1][0]
# print(v, y)

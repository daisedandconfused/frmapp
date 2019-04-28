import numpy as np


def previousevent(n):

    # creates matrix with zeros in (# of rows, # of columns)
    p = np.zeros(((2**(n-2)), n-2))
    a = p.shape[0]
    b = p.shape[1]

    for k in range(0, b, 1):
        z = int((a/(2**k))-1)
        for i in range(0, a, 2**(b+1-k)):
            for j in range(0, z, 1):
                p[i+j][k] = 1
        x = int((a/(2**k))+1)
        for i in range(x, a, (2**b)+1-k):
            for j in range(0, z, 1):
                p[i+j][k] = 2

    return p


v = previousevent(n=4)

print(v)

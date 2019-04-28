from personconsq.doors import *
from prevevent import previousevent as pe
import numpy as np

def v4(door_stair):

    n = 4
    v = pe(n)

    d2 = stair(door_stair)
    p = np.zeros((len(v), 1))

    for i in range(0, len(v)):
        if v[i][0] == 1:  # autsup successful
            p[i] = 0
        else:
            if v[i][1] == 1:  # apt door successful
                p[i] = 0
            else:
                p[i] = d2[0]

    b4 = [[1-d2[0]], [d2[0]]]

    return b4

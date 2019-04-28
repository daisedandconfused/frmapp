from personconsq.doors import *
from prevevent import previousevent as pe
import numpy as np

def v5s4(door_air):

    n = 5
    v = pe(n)

    d3 = airlock(door_air)
    p = np.zeros((len(v), 1))

    for i in range(0, len(v)):
        if v[i][0] == 1 or v[i][1] == 1 or v[i][2] == 1:  # autsup or any prev door successful
            p[i] = 0
        else:
            p[i] = d3[0]

    b5 = [[1-d3[0]], [d3[0]]]

    return b5

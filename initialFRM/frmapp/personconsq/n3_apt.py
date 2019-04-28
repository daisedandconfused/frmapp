from personconsq.doors import apt
from prevevent import previousevent as pe
import numpy as np

def v3(door_apt):

    n = 3
    v = pe(n)

    d1 = apt(door_apt)
    p = np.zeros((len(v), 1))

    for i in range(0, len(v)):
        if v[i][0] == 1:  # autsup successful
            p[i] = 0
        elif v[i][0] == 2:  # autsup unsuccessful
            p[i] = d1[0]

    b3 = [[1-d1[0]], [d1[0]]]

    return b3


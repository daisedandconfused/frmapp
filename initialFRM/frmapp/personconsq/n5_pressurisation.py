import math
from prevevent import previousevent as pe
import numpy as np

def v5(h_max):
    """
    this function calculates the probability of the pressurisation
    system to fail.
    :param h_max: the building height affects the effectiveness of
    the pressurisation system (stack effect)
    :return: probability of the activation/effectiveness failure of
    the system.
    """
    h = h_max / 2
    pf_act = 0.1
    pf_eff = 0.2 * math.log(h)

    pf = pf_act + pf_eff - (pf_act*pf_eff)

    # if the door is open, PF = 1

    n = 5
    v = pe(n)
    p = np.zeros((len(v), 1))

    for i in range(0, len(v)):
        if v[i][0] == 1:  # autsup successful
            p[i] = 0
        else:
            if v[i][1] == 1 or v[i][2] == 1:  # any door successful
                p[i] = pf
            elif v[i][2] == 2: # lobby door unsuccessful
                p[i] = 1

    # there seems to be no effect, as the pressurisation if fact
    # doesnt work if the previous barrier fails.

    b5 = [[1-pf], [pf]]

    return b5

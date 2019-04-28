from prevevent import previousevent as pe
import numpy as np
from n2_autsup import autosup as n2


def compartment(n):
    """
    Calculates the probability of fire spread beyond the fire
    compartent.
    :param n: node number
    :return p: the conditional probability of failure of confinement to room of origin
    :param pf_c: the portion of fires that spread beyond compartment of origin
    given spread beyond room.
    """
    pf_c = 0.95

    v = pe(n)
    lv = len(v)
    # failure probability vector:
    p = np.zeros((lv, 1))

    for i in range(0, lv):
        if v[i][0] == 1:  # autsup successful
            p[i] = 0
        elif v[i][0] == 2:  # autsup unsuccessful
            p[i] = pf_c

    return p


def n3v(n):

    p = compartment(n)

    l = 2**(n-1)
    b3 = np.ones((l, 1))

    b3[0][0] = 1 - p[0][0]
    b3[1][0] = p[0][0]
    b3[2][0] = 1 - p[1][0]
    b3[3][0] = p[1][0]

    # vector containing only relevant values
    # res3 = [[1-p], [p]]
    p3 = [x for x in b3 if x not in[0, 1]]

    return p3


#p3 = n3v(n=3, spr=1)

#k = len(p3)

#print(p3, k)


# prob0 = autosup(spr)
# prob1 = compartment(prob0)
# print("The probability of failure to contain the fire in the compartment of origin: {}".format(prob1))

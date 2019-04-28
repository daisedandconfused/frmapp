import math
from prevevent import previousevent as pe
import firespread.firefighters as ff
import numpy as np


def storey(sh, fs):
    """
    ONLY if all previous barriers have failed.
    function calculating the probability of the fire to spread externally
    along the facade.
    :param sh: spandrel height of the facade in m
    :param h_max: building height (unused???)
    :param fs: variable from user-input indicating the type of facade (traditional/modern)
    :return: pf = probability of external firespread
    """
    """
    In the second part, a vector of size len(previous event vector)=4 is 
    created, containing the probability of spread beyond storey
    conditioned by whether or not autosupression or 
    compartmentalisation is successful.
    In case one of them succeeds, failure prob is 0. If both fail,
    there is a failure probability pf*pff.
    it is assumed, that intervention time t is 30 minutes.
    """

    # heat flux
    q = 16 * math.log(sh)

    # exterior spread
    if fs == 1 and q < 12.5:
        p = 0
    elif fs == 1 and q < 25:
        p = (1 / 12.5) * q - (12.5 / 12.5)
    else:
        p = 1

    return p


def vector(sh, fs, n, glass, t):

    v = pe(n)
    # failure probability fire-service:
    pff = ff.fireservice(fs, glass, n, t)
    # failure probability compartment:
    pf = storey(sh, fs)

    pf_s = np.zeros((len(v), 1))
    for i in range(0, len(v)):
        # if spr fail and comp fail:
        if v[i][0] == 2 and v[i][1] == 2:
            pf_s[i] = pf * pff[i]
        else:
            pf_s[i] = 0

    return pf_s


def n4v(n, sh, fs, glass, t):

    pf_s = vector(sh, fs, n, glass, t)

    l = 2**(n-1)  # =8
    b4 = np.ones((l, 1))

    b4[0][0] = 1 - pf_s[0][0]
    b4[1][0] = pf_s[0][0]
    b4[2][0] = 1 - pf_s[1][0]
    b4[3][0] = pf_s[1][0]
    b4[4][0] = 1 - pf_s[2][0]
    b4[5][0] = pf_s[2][0]
    b4[6][0] = 1 - pf_s[3][0]
    b4[7][0] = pf_s[3][0]

    # vector containing only relevant values
    # res3 = [[1-p], [p]]
    p4 = [x for x in b4 if x not in[0, 1]]

    return p4


# p4 = n4v(n=4, sh=3, fs=1, glass=2, t=30, spr=1)
# print(p4)

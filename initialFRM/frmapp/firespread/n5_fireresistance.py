from scipy.stats import norm
import numpy as np
from prevevent import previousevent as pe


def fireresistance(lbc, n):

    # Probability that fire duration exceeds resistance

    wf = 1.5
    kb = 0.07
    mu = 800
    s = 220

    p = 1-norm.cdf((lbc/(wf*kb)), mu, s)
    v = pe(n)
    pf = np.zeros((len(v), 1))

    for i in range(0, len(v)):
        # if compartmentalisation fails:
        if v[i][1] == 2:
            pf[i] = p
        else:
            pf[i] = 0
    return pf


def n5v(lbc, n):

    pf = fireresistance(lbc, n)

    l = 2**(n-1) #=16
    b5 = np.ones((l, 1))

    b5[0][0] = 1 - pf[0][0]
    b5[1][0] = pf[0][0]
    b5[2][0] = 1 - pf[1][0]
    b5[3][0] = pf[1][0]
    b5[4][0] = 1 - pf[2][0]
    b5[5][0] = pf[2][0]
    b5[6][0] = 1 - pf[3][0]
    b5[7][0] = pf[3][0]
    b5[8][0] = 1 - pf[4][0]
    b5[9][0] = pf[4][0]
    b5[10][0] = 1 - pf[5][0]
    b5[11][0] = pf[5][0]
    b5[12][0] = 1 - pf[6][0]
    b5[13][0] = pf[6][0]
    b5[14][0] = 1 - pf[7][0]
    b5[15][0] = pf[7][0]

    # vector containing only relevant values
    # p5 = [[1-p], [p]] times 4
    p5 = [x for x in b5 if x not in[0, 1]]

    return p5


# p5 = n5v(lbc=120, n=5, spr=0)

# print(p5)

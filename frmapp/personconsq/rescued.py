from scipy.stats import norm
import numpy as np
import math


def res(v, lbc, aba, spr, s_alarm):

    q = 0.8
    tc = norm.ppf(q, a[0][0], a[0][1])
    tca = norm.ppf(q, a[1][0], a[1][1])
    tcs = norm.ppf(q, a[2][0], a[2][1])
    tcsa = norm.ppf(q, a[3][0], a[3][1])

    if ld == 1:
        rl = 0.33
    else:
        rl = 0

    resh = 0.01

    # if spr success & door success
    #   t = lbc - tcs
    #   nres = math.floor((resl + resh)*t)
    # elif spr success & door fail
    #   t = lbc - tcsa
    #   nres = math.floor((resl + resh)*t)
    # elif spr fail & door success
    #   t = lbc - tc
    #   nres = math.floor((resl + resh)*t)
    # elif spr fail & door fail
    #   t = lbc - tca
    #   nres = math.floor((resl + resh)*t)

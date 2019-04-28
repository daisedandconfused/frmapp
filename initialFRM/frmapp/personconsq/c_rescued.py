from scipy.stats import norm
from personconsq.c_arrivalfs import *
from notcall import notcall
from userinput import Building
import numpy as np
import math
from prevevent import previousevent as pe


def res(resop, lbc, a, x):

    q = 0.8
    tc = norm.ppf(q, a[0][0], a[0][1])
    tca = norm.ppf(q, a[1][0], a[1][1])
    tcs = norm.ppf(q, a[2][0], a[2][1])
    tcsa = norm.ppf(q, a[3][0], a[3][1])

    if resop == 1:
        resl = 0.33
    else:
        resl = 0

    resh = 0.01

    nres = np.ones((len(x), 1))

    for i in range(0, len(x)):
        # if spr success & door success
        if x[i][0] == 1 and x[i][1] == 1:
            t = lbc - tcs
            nres[i] = math.floor((resl + resh)*t)
        # elif spr success & door fail
        elif x[i][0] == 1 and x[i][1] == 2:
            t = lbc - tcsa
            nres[i] = math.floor((resl + resh)*t)
        # elif spr fail & door success
        elif x[i][0] == 2 and x[i][1] == 1:
            t = lbc - tc
            nres[i] = math.floor((resl + resh)*t)
        # elif spr fail & door fail
        elif x[i][0] == 2 and x[i][1] == 2:
            t = lbc - tca
            nres[i] = math.floor((resl + resh)*t)

    return nres


# b = Building()
# spr, a, c0, ns, apps, npa, y, h_max, stw, layout, door_air, door_apt, door_stair, sh, ele, s_alarm, aba, fs, glass, warn, lbc, resop = b.demo()

# call = notcall(s_alarm)

# fnot_s, fnot_a, n1, n2, n3, n4 = notification(spr, aba, call)

# a = arrival(aba, spr, n1, n2, n3, n4)

# nres = res(resop, lbc, a)

# print(nres)

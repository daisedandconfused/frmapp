from personconsq.c_arrivalfs import *
from notcall import notcall
import math


def warningt(warn, ele, ns, a):

    # no warning system: evacuation by personal message
    if warn == 0:
        if ele == 0:
            up = 1 / 30 * ns
        else:
            up = 0.3 * ns
        w_all = up + 5 * ns
        prep = w_all / 2
        sigma1 = 0.15 * w_all

        m = [[a[0][0], (math.sqrt(a[0][1]**2 + sigma1**2))],
             [a[1][0] + prep, (math.sqrt(a[0][1]**2 + sigma1**2))],
             [a[2][0] + prep, (math.sqrt(a[0][1]**2 + sigma1**2))],
             [a[3][0] + prep, (math.sqrt(a[0][1]**2 + sigma1**2))]]

    # manual warning system
    elif warn == 1:
        prep = 5

        m = [[a[0][0] + prep, a[0][1]],
             [a[1][0] + prep, a[1][1]],
             [a[2][0] + prep, a[2][1]],
             [a[3][0] + prep, a[3][1]]]

    # automatic warning system
    else:
        s = 1
        mu = 5

        m = [[mu, s], [mu, s], [mu, s], [mu, s]]

    return m


# b = Building()
# spr, a, c0, ns, apps, npa, y, h_max, stw, layout, door_air, door_apt, door_stair, sh, ele, s_alarm, aba, fs, glass, warn, lbc, resop = b.demo()

# call = notcall(s_alarm)

# fnot_s, fnot_a, n1, n2, n3, n4 = notification(spr, aba, call)

# a = arrival(aba, spr, n1, n2, n3, n4)

# wt = warningt(warn, ele, ns, a)

# print(wt)

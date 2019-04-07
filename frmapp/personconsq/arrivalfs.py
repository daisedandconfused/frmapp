from firespread.notcall import notcall
from firespread.userinput import *
from firespread.approxnorm import *


def notification(spr, aba, call):

    if spr == 1:
        fnot_s = 0.01
    else:
        fnot_s = 1

    if aba == 1:
        fnot_a = 0.1 + 0.9 * 0.01
    else:
        fnot_a = 1

    n1 = call
    n2 = call * fnot_a
    n3 = call * fnot_s
    n4 = call * fnot_a * fnot_s

    return fnot_s, fnot_a, n1, n2, n3, n4


def arrival(aba, spr):

    t1 = 15
    t2 = 15

    sf = 2.7

    psc = 1 - n1
    sigmac = 6
    muc = appnorm(t2, psc, sigmac)

    psca = 1 - n2
    if aba == 1:
        sigmaca = sf
    else:
        sigmaca = sigmac
    muca = appnorm(t1, psca, sigmaca)

    pscs = 1 - n3
    if spr == 1:
        sigmacs = sf
    else:
        sigmacs = sigmac
    mucs = appnorm(t1, pscs, sigmacs)

    pscsa = 1 - n4
    if spr == 1 and aba == 1:
        sigmacsa = sf
    else:
        sigmacsa = sigmac
    mucsa = appnorm(t1, pscsa, sigmacsa)

    s = [[muc, sigmac], [muca, sigmaca], [mucs, sigmacs], [mucsa, sigmacsa]]

    return s

b = Building()

spr, a, ns, apps, y, h_max, stw, layout, door_air, door_apt, door_stair, sh, ele, s_alarm, aba, fs, glass, warn, lbc = b.demo()

call = notcall(s_alarm)

fnot_s, fnot_a, n1, n2, n3, n4 = notification(spr, aba, call)

ss = arrival(aba, spr)

print(ss)

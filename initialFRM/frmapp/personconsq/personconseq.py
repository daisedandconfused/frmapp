from personconsq import c_arrivalfs as c_a, c_rescued as c_r, c_smokestairtime as c_s, c_warningtime as c_w
from notcall import notcall
import personconsq.doors as d
import approxnorm as an
import numpy as np
import math
from prevevent import previousevent as pe
from userinput import Building
from scipy.stats import norm


def nrescued(layout):
    """
    :param layout: indicates type of stair layout
    :return: number of event combos/scenarios
    """
    # direct access
    if layout == 1:
        sc = 0
        x = pe(4)
    # with lobby
    elif layout == 2:
        sc = 1
        x = pe(5)
    # pressurised
    elif layout == 3:
        sc = 3
        x = pe(6)
    # airlock
    elif layout == 4:
        sc = 6
        x = pe(7)

    return sc, x


def travel(nres, stw, sc, ns, apps, npa):

    ntot = ns * apps * npa

    p = np.ones((4, 1))
    p[0] = (ntot - nres[0])/(stw - 0.3)
    p[1] = (ntot - nres[2+sc])/(stw - 0.3)
    p[2] = (ntot - nres[3+2*sc])/(stw - 0.3)
    p[3] = (ntot - nres[4+3*sc])/(stw - 0.3)

    sigma_move = 0.26
    t1 = 0.68 + 0.081 * (p[0])**0.73
    t2 = 0.68 + 0.081 * (p[1])**0.73
    t3 = 0.68 + 0.081 * (p[2])**0.73
    t4 = 0.68 + 0.081 * (p[3])**0.73

    # t = [[t1][t2][t3][t4]]
    mu_move = np.ones((4, 1))
    mu_move[0] = an.appnorm(t1, 0.0001, sigma_move)
    mu_move[1] = an.appnorm(t2, 0.0001, sigma_move)
    mu_move[2] = an.appnorm(t3, 0.0001, sigma_move)
    mu_move[3] = an.appnorm(t4, 0.0001, sigma_move)

    return mu_move


def combo(m, mu_move):

    sigma_move = 0.26

    # CALL
    muc = m[0][0] + mu_move[0]
    scc = math.sqrt((m[0][1])**2 + sigma_move**2)

    # CALL&ABA
    muca = m[1][0] + mu_move[1]
    sca = math.sqrt((m[1][1])**2 + sigma_move**2)

    # CALL&SPR
    mucs = m[2][0] + mu_move[2]
    scs = math.sqrt((m[2][1])**2 + sigma_move**2)

    # CALL&SPR&ABA
    mucsa = m[3][0] + mu_move[3]
    scsa = math.sqrt((m[3][1])**2 + sigma_move**2)

    return muc, scc, muca, sca, mucs, scs, mucsa, scsa


def consequences(spr, x, t, muc, scc, muca, sca, mucs, scs, mucsa, scsa, ntot, nres):

    if spr == 1:
        fred = 0.3
    else:
        fred = 1

    pf = np.zeros((len(x), 1))
    consq = np.zeros((len(x), 1))

    for i in range(0, len(x)):
        # if spr success & door success
        if x[i][0] == 1 and x[i][1] == 1:
            pf[i] = 1 - norm.cdf(t[i], mucs, scs)
            consq[i] = math.ceil(pf[i] * (ntot - nres[i]) * fred)

        # if spr success & door fail
        if x[i][0] == 1 and x[i][1] == 2:
            pf[i] = 1 - norm.cdf(t[i], mucsa, scsa)
            consq[i] = math.ceil(pf[i] * (ntot - nres[i]) * fred)

        # if spr fail & door success
        if x[i][0] == 2 and x[i][1] == 1:
            pf[i] = 1 - norm.cdf(t[i], muc, scc)
            consq[i] = math.ceil(pf[i] * (ntot - nres[i]))

        # if spr fail & door fail
        if x[i][0] == 2 and x[i][1] == 2:
            pf[i] = 1 - norm.cdf(t[i], muca, sca)
            consq[i] = math.ceil(pf[i] * (ntot - nres[i]))

    return consq

"""

b = Building()
spr, a, c0, ns, apps, npa, y, h_max, stw, layout, door_air, door_apt, door_stair, sh, ele, s_alarm, aba, fs, glass, warn, lbc, resop = b.demo()

ntot = ns * apps * npa

sc, x = nrescued(layout)

# run event 1
call = notcall(s_alarm)

# run event 2 & 3
fnot_s, fnot_a, n1, n2, n3, n4 = c_w.notification(spr, aba, call)

arriv = c_a.arrival(aba, spr, n1, n2, n3, n4)

# number of ppl rescued
nres = c_r.res(resop, lbc, arriv, x)

# time to warn
wt = c_w.warningt(warn, ele, ns, arriv)

# consequence calcs

mu_move = travel(nres, stw, sc, ns, apps, npa)

muc, scc, muca, sca, mucs, scs, mucsa, scsa = combo(wt, mu_move)

# smokestairtime

d1 = d.apt(door_apt)
d2 = d.stair(door_stair)
d3 = d.airlock(door_air)

d = [d1, d2, d3]

t = c_s.smoketime(layout, d)

c = consequences(spr, x, t, muc, scc, muca, sca, mucs, scs, mucsa, scsa)

print("The consequences associated with each scenario for layout {} are: \n {}".format(layout, c))

"""

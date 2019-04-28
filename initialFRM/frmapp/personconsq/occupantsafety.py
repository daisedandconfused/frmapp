from n1_fire import fire as n1
from n2_autsup import autosup as n2
from personconsq.n3_apt import v3 as n3
from personconsq.n4_lobby import v4 as n4
from personconsq.n5_pressurisation import v5 as n5
from personconsq.n5s4_AL import v5s4 as n5s4
from personconsq.n6s4_airlock import v6s4 as n6s4
from personconsq.personconseq import *
from personconsq import c_arrivalfs as c_a, c_rescued as c_r, c_smokestairtime as c_s, c_warningtime as c_w
from notcall import notcall
import personconsq.doors as d
import numpy as np
from prevevent import previousevent as pe
from userinput import Building


# k_prob = saff(saf)

"""
small fires
"""

r0 = n1(0)*0.04

"""
large fires
"""

#b = Building()
#spr, a, c0, ns, apps, npa, y, h_max, stw, layout, door_air, door_apt, door_stair, sh, ele, s_alarm, aba, fs, glass, warn, lbc, resop = b.demo()

"""
consequence vector
"""
ns = 30
apps = 5
npa = 4

ntot = ns * apps * npa

sc, x = nrescued(4)

# run event 1
call = notcall(1)

# run event 2 & 3
fnot_s, fnot_a, x1, x2, x3, x4 = c_w.notification(1, 0, call)

arriv = c_a.arrival(0, 1, x1, x2, x3, x4)

# number of ppl rescued
nres = c_r.res(1, 120, arriv, x)

# time to warn
wt = c_w.warningt(2, 0, ns, arriv)

# consequence calcs

mu_move = travel(nres, 2, sc, ns, apps, npa)

muc, scc, muca, sca, mucs, scs, mucsa, scsa = combo(wt, mu_move)

# smokestairtime

d1 = d.apt("UC-C")
d2 = d.stair("EI30-C")
d3 = d.airlock("EI30")

d = [d1, d2, d3]

t = c_s.smoketime(4, d)

c = consequences(1, x, t, muc, scc, muca, sca, mucs, scs, mucsa, scsa, ntot, nres)

"""
Probability vector
"""
# nodes

n2 = n2(1)
n3 = n3("UC-C")
n4 = n4("EI30-C")
n5 = n5(100)
n5s4 = n5s4("EI30")
n6s4 = n6s4(100)


def probability(layout):

    # for all: sprinkler success
    r1 = n2[0]

    if layout == 1:
        n = 4
        v = pe(n)
        r = np.zeros((len(v), 1))

        for i in range(0, len(v)):
            # spr success
            if v[i][0] == 1:
                r[i] = r1
            else:
                # apt door success
                if v[i][1] == 1:
                    r[i] = n2[1][0]*n3[0][0]
                else:
                    # apt door failure
                    r[i] = n2[1][0]*n3[1][0]

    elif layout == 2:
        n = 5
        v = pe(n)
        r = np.zeros((len(v), 1))

        for i in range(0, len(v)):
            # spr success
            if v[i][0] == 1:
                r[i] = r1
            else:
                # apt door success
                if v[i][1] == 1:
                    r[i] = n2[1][0]*n3[0][0]
                else:
                    # lobby door success
                    if v[i][2] == 1:
                        r[i] = n2[1][0]*n3[1][0]*n4[0][0]
                    else:
                        # lobby door failure
                        r[i] = n2[1][0]*n3[1][0]*n4[1][0]

    elif layout == 3:
        n = 6
        v = pe(n)
        r = np.zeros((len(v), 1))
        for i in range(0, len(v)):
            # spr success
            if v[i][0] == 1:
                r[i] = r1
            else:
                # apt door success
                if v[i][1] == 1:
                    r[i] = n2[1][0]*n3[0][0]
                else:
                    # lobby door and press success
                    if v[i][2] == 1 and v[i][3] == 1:
                        r[i] = n2[1][0]*n3[1][0]*n4[0][0]*n5[0][0]
                    # lobby door success and press failure
                    elif v[i][2] == 1 and v[i][3] == 2:
                        r[i] = n2[1][0]*n3[1][0]*n4[0][0]*n5[1][0]
                    # lobby door failure
                    else:
                        r[i] = n2[1][0]*n3[1][0]*n4[1][0]

    if layout == 4:
        n = 7
        v = pe(n)
        r = np.zeros((len(v), 1))

        for i in range(0, len(v)):
            # spr success
            if v[i][0] == 1:
                r[i] = r1
            else:
                # apt door success
                if v[i][1] == 1:
                    r[i] = n2[1][0]*n3[0][0]
                else:
                    # lobby door success
                    if v[i][2] == 1:
                        r[i] = n2[1][0]*n3[1][0]*n4[0][0]
                    else:
                        # AL door success
                        if v[i][3] == 1:
                            r[i] = n2[1][0]*n3[1][0]*n4[1][0]*n5s4[0][0]
                        else:
                            # AL system success
                            if v[i][4] == 1:
                                r[i] = n2[1][0]*n3[1][0]*n4[1][0]*n5s4[1][0]*n6s4[0][0]
                            # AL system failure
                            else:
                                r[i] = n2[1][0]*n3[1][0]*n4[1][0]*n5s4[1][0]*n6s4[1][0]

    return r

# number of fires:
nf = 2 * 10**(-5) * 1000 * ns * 20

# probability
r = probability(4)
ri = (r*c)
risk = nf * (int(r0 + n1(1)*sum(ri)))

years = 20

print("\n The Risk (associated occupant loss) for this design"
      "\n in the specified time-frame of {} years is {} injuries or fatalities, "
      "\n corresponding to an expected {} fires in total.".format(years, risk, nf))


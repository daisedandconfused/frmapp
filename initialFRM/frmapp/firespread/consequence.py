from firespread.userinput_propertyloss import Building
from n1_fire import fire as n1
from n2_autsup import autosup as n2
from firespread.n3_compartment import n3v as n3
from firespread.n4_storey import n4v as n4
from firespread.n5_fireresistance import n5v as n5


def saff(saf):

    # eventually specify safety factors y
    if saf == 2:
        k_prob = 2
    else:
        k_prob = 1
    return k_prob


b = Building()
spr, a, c0, ns, apps, npa, y, saf, stw, sh, ele, s_alarm, aba, fs, glass, warn, lbc = b.demo()

# autosuppression
ip2 = n2(spr=spr)
# compartment
ip3 = n3(n=3)
# storey
ip4 = n4(n=4, sh=sh, fs=fs, glass=glass, t=30)
# fire resistance - only if comp fails
ip5 = n5(lbc=lbc, n=5)
# safety factor
k_prob = saff(saf)

"""
consequences
"""
c_room = a * c0/apps * 1/5
c_comp = a * c0/apps
c_storey = a * c0
c_half = ns/2 * a * c0
c_tot = ns * a * c0

"""
small fires
"""
cq = 0
r0 = n1(0)*k_prob*cq

"""
large fires
"""
# spr success
r1 = ip2[0][0]*k_prob*c_room
# comp success
r2 = ip2[1][0]*ip3[0][0]*k_prob*c_comp
# storey and fire res success
r3 = (ip2[1][0]*ip3[1][0])*ip4[0][0]*ip5[0][0]*k_prob*c_storey
# storey success, fire res fail
r4 = (ip2[1][0]*ip3[1][0])*ip4[0][0]*ip5[1][0]*k_prob*c_tot
# storey fail, fire res success
r5 = (ip2[1][0]*ip3[1][0])*ip4[1][0]*ip5[0][0]*k_prob*c_half
# both storey and fire res fail
r6 = (ip2[1][0]*ip3[1][0])*ip4[1][0]*ip5[1][0]*k_prob*c_tot

# risk of each large fire scenario per fire (vector)
values = [r1, r2, r3, r4, r5, r6]

# number of fires:
nf = 2 * 10**(-5) * a * ns * y

risk = nf * (int(r0 + n1(1)*sum(values)))

years = y

print("\n The Risk (associated monetary loss) for this design"
      "\n in the specified time-frame of {} years is {} GPB, "
      "\n corresponding to an expected {} fires in total.".format(y, risk, nf))

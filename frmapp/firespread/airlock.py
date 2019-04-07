import math

def airlock_fail(h_max):

    # wind load based on EC1, 1-4
    h = h_max / 2

    # basic wind speed in m/s
    vb = 24

    # normalisation factor
    vm150 = 10 * 0.2 * math.log(150/0.3) * vb

    pf = 0.2 * math.log(h/0.3) * (vb/vm150)
    return pf

#p = airlock_fail(hmax=100)
#print(p)


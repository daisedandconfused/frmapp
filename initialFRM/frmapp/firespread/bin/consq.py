from prevevent import previousevent as pe
import numpy as np

def consequences(a, c0, apps, ns):

    #number of nodes:
    n = 6

    c_room = a * c0/apps * 1/5
    c_comp = a * c0/apps
    c_storey = a * c0
    c_half = ns/2 * a * c0
    c_tot = ns * a * c0

    v = pe(n)
    c = np.zeros((len(v), 1))

    for i in range(0, len(v)):
        if v[i][0] == 1:
            c[i] = c_room
        elif v[i][1] == 1:
            c[i] = c_comp
        elif v[i][2] == 1 and v[i][3] == 1:
            c[i] = c_storey
        elif v[i][2] == 1 and v[i][3] == 2:
            c[i] = c_tot
        elif v[i][2] == 2 and v[i][3] == 1:
            c[i] = c_half
        else:
            c[i] = c_tot

    return c

"""    
v = vector previousevent(Nn = 6); meaning a 16x4 matrix
i = i:size(v) = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 24, 15, 16]

v(i,1) = row i column 1 == 1 = scenarios 1-8, where sprinkler succeeds
ci = c room (value plugged into all rows in column 1 with value 1)

v(i,2) = row i column 2 == 1 = compartment success
ci = c comp

v(i,3) = row i column 3 == 1 and v(i,4) == 1, storey success, fireresistace success
ci = c storey

v(i,3) = row i column 3 == 1 and v(i,4) == 2, storey success, fireres failure
ci = c total

v(i,3) = row i column 3 == 2 and v(i,4) == 1, storey failure, fireres success
ci = c half

else (all fails)
ci = c total

c = vector of 16 elements containing loss per scenario
"""

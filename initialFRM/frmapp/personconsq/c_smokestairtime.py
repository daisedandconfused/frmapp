from prevevent import previousevent as pe
import numpy as np
from personconsq.doors import *


def smoketime(layout, d):

    # layout options
    # [1] direct access
    # [2] stair connected to lobby
    # [3] pressurised stair connected to lobby
    # [4] stair in connection to an airlock and lobby

    d1 = d[0][1] # apartment door time
    d2 = d[1][1] # stair door time
    d3 = d[2][1] # air lock door time

    # direct access
    if layout == 1:
        v = pe(4)
        t = np.zeros((len(v), 1))
        for i in range(0, len(v)):
            # if spr success
            if v[i][0] == 1:
                t[i]= 60000 # never smoke in stair
            # if spr fail
            else:
                # door 1 success (closed)
                if v[i][1] == 1:
                    t[i] = d1
                # both fail
                else:
                    t[i] = 0

    # stair connected to lobby
    elif layout == 2:
        v = pe(5)
        t = np.zeros((len(v), 1))
        for i in range(0, len(v)):
            #spr success
            if v[i][0] == 1:
                t[i]= 60000 # never smoke in stair
                # spr fail
            else:
                # door 1 closed
                if v[i][1] == 1 and v[i][2] == 1:
                    t[i] = d1 + d2
                elif v[i][1] == 1 and v[i][2] == 2:
                    t[i] = d1
                elif v[i][1] == 2 and v[i][2] == 1:
                    t[i] = d2
                else:
                    t[i] = 0

    # pressurised stair connected to lobby
    elif layout == 3:
        v = pe(6)
        t = np.zeros((len(v), 1))
        for i in range(0, len(v)):
            # spr success or pressurisation success
            if v[i][0] == 1 or (v[i][3] == 1 and v[i][2] == 1):
                t[i] = 60000 # never smoke in stair
            else:
                # both doors closed
                if v[i][1] == 1 and v[i][2] == 1:
                    t[i] = d1 + d2
                # door 1 closed
                elif v[i][1] == 1 and v[i][2] == 2:
                    t[i] = d1
                # door 2 closed
                elif v[i][1] == 2 and v[i][2] == 1:
                    t[i] = d2
                # all fails:
                else:
                    t[i] = 0

    # stair in connection to an airlock and lobby
    elif layout == 4:
        v = pe(7)
        t = np.zeros((len(v), 1))
        for i in range(0, len(v)):
            # spr success or airlock success
            if v[i][0] == 1 or v[i][4] == 1:
                t[i] = 60000 # never smoke in stair
            else:
                # all doors closed
                if v[i][1] == 1 and v[i][2] == 1 and v[i][3] == 1:
                    t[i] = d1 + d2 + d3
                # door 1 closed and door 2 closed
                elif v[i][1] == 1 and v[i][2] == 1 and v[i][3] == 2:
                    t[i] = d1 + d2
                # door 1 closed and door 3 closed
                elif v[i][1] == 1 and v[i][2] == 2 and v[i][3] == 1:
                    t[i] = d1 + d3
                # door 2 closed and door 3 closed
                elif v[i][1] == 2 and v[i][2] == 1 and v[i][3] == 1:
                    t[i] = d2 + d3
                # door 1 closed
                elif v[i][1] == 1 and v[i][2] == 2 and v[i][3] == 2:
                    t[i] = d1
                # door 2 closed
                elif v[i][1] == 2 and v[i][2] == 1 and v[i][3] == 2:
                    t[i] = d2
                # door 3 closed
                elif v[i][1] == 2 and v[i][2] == 2 and v[i][3] == 1:
                    t[i] = d3
                # all fails
                else:
                    t[i] = 0
    return t


# d1 = apt(door_apt="UC")
# d2 = stair(door_stair="EI60")
# d3 = airlock(door_air="EI30-C")

# d = [d1, d2, d3]

# t = smoketime(3, d)

# print(t)

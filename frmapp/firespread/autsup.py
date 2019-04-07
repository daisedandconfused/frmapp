# from userinput import Building
from firespread.fire import *

def autosup(spr):
    """
    Calculates the probability of the fire suppression failure

    :param spr: spr is an boolean indicating the presence of sprinkler
    :return: the conditional probability of failure given a large fire
    depending on presence of sprinkler
    """
    # reliability of confinement with sprinkler:
    r0 = 0.97

    # reliability of confinement w/o sprinkler:
    r1 = 0.78

    # probability of a large fire from fire.py
    l = f1

    if spr == 1:    # P(failure) if sprinkler installed
        p = (1 - r0) / l
    else:
        p = (1 - r1) / l   # P(failure) if no sprinkler installed

    return p

# There is no sprinkler installed, given a large fire 44 % = 1-0.56
# is still confined to the room of origin

def compartment(p):
    """
    Calculates the probability of fire spread beyond the fire
    compartent.
    :param p: the probability of failure of confinement to room of origin
    :const c: the portion of fires that spread beyond compartment of origin
    given spread beyond room.
    """
    c = 0.95
    pf = p * c

    return pf

# b = Building()
# s, _, _, _, _, _, _, _, _ = b.demo()

# f1 = fire(i=1) #percantage of large fires

# prob0 = autosup(s)
# print("The probability of failure to contain the fire in the room of origin: {}".format(prob0))

# prob1 = compartment(prob0)
# print("The probability of failure to contain the fire in the compartment of origin: {}".format(prob1))

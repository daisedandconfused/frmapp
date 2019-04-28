# from userinput import *
from prevevent import previousevent as pe
import intervention as int
import numpy as np

def fseff(t, tfo):
    """
    :param t: average time in minutes of fire service intervention
    :param tfo: time of flashover (from fireservice function below) / time
    until window breakage
    :return exeff: probability of effective fire extinguishment.
    """

    i = tfo / 10

    # success probaility of extinguishment before flashover is 100%
    if t < tfo:
        exeff = 1
    else:
        exeff = t / (i * 10**(t / (i * 10)))

    return exeff


def fireservice(fs, glass, n):
    """
    :param fs: type of facade: 0 = traditional, 1 = modern
    :param glass: type of window: single-/double-/triple-paned
    :return: probability of firefighters effectively extinguishing the fire
    """
    # (mean) time in minutes of fire service intervention (from experiments)
    t = 30

    if fs == 0:
        if glass == 1:
            p_eff = fseff(t, 10)
        elif glass == 2:
            p_eff = fseff(t, 20)
        elif glass == 3:
            p_eff = fseff(t, 30)
    # for a modern (curtain wall) facade, flashover happens within 10 minutes,
    # regardless of window type.
    else:
        p_eff = fseff(t, 10)

    """
    Here, a vector of size len(previous event vector) is 
    created, containing the probability of fire service intervention
    failure, conditioned by whether or not autosupressio is succesful.
    In case of successful autosup, failure prob is 0.
    it is assumed, that intervention time t is 30 minutes.
    """
    p_int = int.combine(t)
    p = pe(n)

    ffail = np.zeros((len(p), 1))
    for i in range(0, len(p)):
        if p[i][0] == 2:
            ffail[i] = 1 - (p_int*p_eff)
        else:
            ffail[i] = 0

    return ffail


# p_fail = fireservice(fs=0, glass=2, n=4, t=30)

# print(p_fail)

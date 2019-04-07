from firespread.userinput import *


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


def fireservice(fs, glass):
    """
    :param fs: type of facade: 0 = traditional, 1 = modern
    :param glass: type of window: single-/double-/triple-paned
    :return: probability of firefighters effectively extinguishing the fire
    """
    # (mean) time in minutes of fire service intervention (from experiments)
    t = 30

    if fs == 0:
        if glass == 1:
            peff = fseff(t, 10)
        elif glass == 2:
            peff = fseff(t, 20)
        elif glass == 3:
            peff = fseff(t, 30)
    # for a modern (curtain wall) facade, flashover happens within 10 minutes,
    # regardless of window type.
    else:
        peff = fseff(t, 10)

    return peff

    # in case of sprinkler failure only (no auto suppression)

    fail = 1 - (pint * peff)

b = Building()
_, _, _, _, _, _, _, _, _, _, _, _, ele, s_alarm, aba, fs, glass, warn, lbc = b.demo()

pint = asds()



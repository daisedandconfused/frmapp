import math

def pressurisation(h_max):
    """
    this function calculates the probability of the pressurisation
    system to fail.
    :param h_max: the building height affects the effectiveness of
    the pressurisation system (stack effect)
    :return: probability of the activation/effectiveness failure of
    the system.
    """
    h = h_max / 2
    pf_act = 0.1
    pf_eff = 0.2 * math.log(h)

    # if the door is open, PF = 1

    return pf_act, pf_eff

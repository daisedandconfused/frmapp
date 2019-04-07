import math

def storey(sh, h_max, fs):
    """
    ONLY if all previous barriers have failed.
    function calculating the probability of the fire to spread externally
    along the facade.
    :param sh: spandrel height of the facade in m
    :param h_max: building height (unused???)
    :param fs: variable from user-input indicating the type of facade (traditional/modern)
    :return: p = probability of external firespread
    """

    # heat flux
    q = 16 * math.log(sh)

    # exterior spread
    if fs == 1:     # traditional facade
        if q < 12.5:
            p = 0
        elif q < 25:
            p = (1 / 12.5) * q - (12.5 / 12.5)
        else:
            p = 1
    elif fs == 2:    # modern facade
        p = 1

    return p


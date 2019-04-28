from scipy.special import erfinv
import math


def appnorm(t, ps, sigma):
    """
    Function calculating the approxnorm of a given distribution
    """
    erfx = 2 * ps - 1
    y = erfinv(erfx)

    mu = t - y * math.sqrt(2 * sigma**2)

    return mu



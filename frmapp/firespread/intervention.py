from firespread.notcall import *
from firespread.userinput import *
from firespread import approxnorm
import math
from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt


def asds(aba):
    """
    this function calculates the failure rate of the ASDS (automatic smoke detection system)
    :param aba: indicating presence of ASDS from userinput
    distribution Call + ASDS
    :param psa: probability of success of early notification by telephone or ASDS
    :return: the distribution parameters for success of early notification
    """

    # failure rate given open door
    if aba == 1:
        ab = 0.1 * (0.1 + 0.9 * 0.01) + 0.9
        sigmaca = 1.5

    # failure rate when no ASDS present
    elif aba == 0:
        ab = 1
        sigmaca = 5

    psa = 1 - nocall * ab

    muca = approxnorm.appnorm(15, psa, sigmaca)

    return muca, sigmaca


def setup(ele, ns):
    """
    function calculating the setup time in minutes.
    :param ns: number of storeys specified in user-input
    :return: setup time mean and (standard) deviation
    """
    n = ns / 2

    if ele == 0:
        # no fire-fighting elevator - using stairs
        t_info = 6
        t_travel = 0.3 * n
        t_prep = 0.25 * n
    elif ele == 1:
        # using elevator
        t_info = 8.5
        t_travel = (1 / 30) * n
        t_prep = 0.25 * n

    mu = t_prep + t_travel + t_info

    sigma = 0.35 * mu

    # set = (mu, sigma)

    return set, mu, sigma


# combining distributions

def combine():
    """
    :return: the combined normal cumulative probability function
    """

    t = np.linspace(0, 50, 10000)

    mu_ica = muca + mu
    sigma_ica = math.sqrt(sigmaca**2 + sigma**2)
    print(mu_ica, sigma_ica)

    plt.plot(norm.cdf(t, mu_ica, sigma_ica), 'r-', label='intervention CDF')
    plt.legend()
    plt.show()
    # in matlab: normcdf(x, mu, sigma) = normcdf(t, mu_ica, sigma_ica)

    return pint, proc


b = Building()
_, _, ns, _, _, _, _, _, _, _, _, _, ele, s_alarm, aba, fs, glass, warn, lbc = b.demo()

nocall = notcall(s_alarm)

muca, sigmaca = asds(aba)

s, mu, sigma = setup(ele, ns)

pint, proc = combine()

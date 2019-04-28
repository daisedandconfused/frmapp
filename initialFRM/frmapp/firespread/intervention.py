import notcall as nc
import approxnorm
import math
from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt


def asds(aba, s):
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

    psa = 1 - nc.notcall(s) * ab

    muca = approxnorm.appnorm(15, psa, sigmaca)

    return sigmaca, muca


def setup(ele, ns):
    """
    function calculating the setup time in minutes.
    :param ns: number of storeys specified in user-input
    :return: setup time mean and (standard) deviation
    """
    # average height of fire
    n = ns / 2

    if ele == 0:
        # no fire-fighting elevator - using stairs
        t_info = 6
        t_travel = 0.3 * n
        t_prep = 0.25 * n

        muset = t_prep + t_travel + t_info
        sigmaset = 0.35 * muset

    elif ele == 1:
        # using elevator
        t_info = 8.5
        t_travel = (1 / 30) * n
        t_prep = 0.25 * n

        muset = t_prep + t_travel + t_info
        sigmaset = 0.35 * muset

    return muset, sigmaset


def combine(t):
    """
    combines the distributions of calling and setup
    :return: the combined normal cumulative probability function
    """

#    t = np.linspace(0, 50, 1000)

    mu_ica = muca + muset
    sigma_ica = math.sqrt(sigmaca**2 + sigmaset**2)

    p_int = norm.cdf(t, mu_ica, sigma_ica)

    # this code plots the time-p(int) distribution.
    # However, need to specify a range (t=linspace(x,y,z)) for t to get curve
    # plt.plot(norm.cdf(t, mu_ica, sigma_ica), 'r-', label='intervention CDF')
    # plt.legend()
    # plt.show()

    return p_int


muca, sigmaca = asds(aba=1, s=0)

muset, sigmaset = setup(ele=1, ns=25)

# print(muca, sigmaca, muset, sigmaset)
# print(p_int)

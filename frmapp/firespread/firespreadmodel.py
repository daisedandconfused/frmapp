from firespread.doors2 import *
from firespread.autsup import *

def fire_freq(area, no_storeys, years):
    """
    This function gives the expected number of fires for the specified
    floor area, number of storeys and time-frame in years.

    :param area: area per floor from user input in m^2
    :param no_storeys: number of storeys from user input
    :param years: time-frame in analysis
    :return: number of fires
    """
    no_fire = area * no_storeys * years * 2 * 10**(-5)
    return no_fire

b = Building()

spr, a, ns, y, h_max, layout, door_apt, door_stair, door_air, sh, ele, s_alarm, aba, fs = b.demo()

freq = fire_freq(area=a, no_storeys=ns, years=y)

print("The total number of fires in this design in this time-frame is: {}".format(freq))

# small fires
# cannot spread - giving the number of small fires:

sf = freq * f0
inj = sf * 0.04

print("The number of small fires is: {} and the total number of injuries is therefor {}.".format(sf, inj))

# large fires

lf = freq * f1

print("The number of large fires is {}".format(lf))

# firespread

prob0 = autosup(spr)
print("The probability of failure to contain the fire in the room of origin, given a large fire, is {}".format(prob0))

prob1 = compartment(prob0)
print("The probability of failure to contain the fire in the compartment of origin is {}".format(prob1))

p = prob1 * freq
print("The number of fires spreading beyond the compartment of origin is consequently {}".format(p))

pf_apt, ft_apt = apt(door_apt)
pf_stair, ft_stair = stair(door_stair)
pf_air, ft_air = airlock(door_air)

sbapt = p * pf_apt
sbstair = p * pf_apt * pf_stair

print("The number of fires spreading beyond the apartment door is {}".format(sbapt))
print("The number of fires spreading to the stairwell is {}".format(sbstair))



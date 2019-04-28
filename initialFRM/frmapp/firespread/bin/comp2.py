from userinput import Building
from n2_autsup import autosup

def compartment(i, pf):

    pff = 0.95     # probability of f

    if pf == 1 and i == 0 or i == 1:    # Large fire & sprinkler was successful or small fire
        p = 0                           # passive barriers do not fail
    else:                               # Large fire & sprinkler fails
        p = pff                         # passive barriers fail 95% of the time


    return p

def compartment_failure(p, f):

    c_f = p * f

    return c_f

def total



b = Building()
s, a, ns, y, _, _, _ = b.demo()

pf = autosup(spr=s)

ff = fire_freq(area=a, no_storeys=ns, years=y)

f1 = fire(i=1, no_fire=freq) #number of small fires

c1 = compartment(i=1, spr=s)
cf1 = compartment_failure(p=c1, f=f1)

print("The probability of failure to contain a fire, given a large fire is: {}".format(cf1))

f2 = fire(i=0, no_fire=freq) #number of large fires

c2 = compartment(i=0, spr=s)
cf2 = compartment_failure(p=c2, f=f2)

print("The number of fires spreading beyond the fire compartment is: {}".format(cf2))









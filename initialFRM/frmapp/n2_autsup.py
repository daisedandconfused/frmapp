import n1_fire as f


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

    # probability of a large fire from n1_fire.py
    l = f.fire(1)

    if spr == 1:    # P(failure) if sprinkler installed
        p = (1 - r0) / l
    else:
        p = (1 - r1) / l   # P(failure) if no sprinkler installed

    p2 = [[1-p], [p]]

    return p2

#p2 = autosup(spr=0)

#print("Scenario 3 is the success of the sprinkler")

# If there is no sprinkler installed, given a large fire 44 % = 1-0.56
# is still confined to the room of origin

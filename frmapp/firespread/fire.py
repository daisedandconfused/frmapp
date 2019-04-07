def fire(i):
    """
    This function calculates the portion of small and large fires
    in the previously calculated expected total number of fires.

    :param i: scenario 0 = small fire; scenario 1 = large fire
    :param no_fire: total number of fires
    :return: total number of small/large fires
    """

    if i == 0:
        # Small fire
        d = 0.61
    elif i == 1:
        # Large fire
        d = 0.39

    return d


f0 = fire(i=0) #percentage of small fires
f1 = fire(i=1) #percantage of large fires


# print("The percentage of small fires in this case is: {}".format(f0))
# print("The percentage of large fires in this case is: {}".format(f1))

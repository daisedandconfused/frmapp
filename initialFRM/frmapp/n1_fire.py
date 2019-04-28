def fire(i):
    """
    This function calculates the portion of small and large fires
    in the previously calculated expected total number of fires.

    :param i: scenario 0 = small fire; scenario 1 = large fire
    :return: total number of small/large fires
    """

    if i == 0:
        # Small fire: scenario 1, ends here.
        p1 = 0.61
    elif i == 1:
        # Large fire
        p1 = 0.39

    return p1


# f0 = fire(i=0) #percentage of small fires
# f1 = fire(i=1) #percantage of large fires


# print("The percentage of small fires in this case is: {}".format(f0))
# print("The percentage of large fires in this case is: {}".format(f1))

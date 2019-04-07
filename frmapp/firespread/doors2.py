def apt(door_apt):
    """
    function calculating the failure time & probability of doors.
    :param door_apt: type of door from userinput
    :return: pf_apt = probability of failure of apartment door
    ft_apt = failure time apartment door
    same for stair door.
    """

    d_ap = 0.1  #Prob. of leaving ap. door open when escaping

    if door_apt == "EI60" or "EI30" or "UC":
        pf_apt = d_ap
    elif door_apt == "EI60-C" or "EI30-C" or "UC-C":
        pf_apt = 0

    if door_apt == "EI60" or "EI60-C":
        ft_apt = 60
    elif door_apt == "EI30" or "EI30-C":
        ft_apt = 30
    elif door_apt == "UC" or "UC-C":
        ft_apt = 0

    return pf_apt, ft_apt

def stair(door_stair):

    d_n = 0.3   #Prob. of failure of unclassified door
    d_nC = 0.2  #Prob. of failure of unclassified door with Closer
    d_fd = 0.3  #Prob. of failure fire door
    d_fdC = 0.2 #Prob. of failure fire door with Closer

    if door_stair == "EI60":
        pf_stair = d_fd
        ft_stair = 60
    elif door_stair == "EI60-C":
        pf_stair = d_fdC
        ft_stair = 60
    elif door_stair == "EI30":
        pf_stair = d_fd
        ft_stair = 30
    elif door_stair == "EI30-C":
        pf_stair = d_fdC
        ft_stair = 30
    elif door_stair == "UC":
        pf_stair = d_n
        ft_stair = 0
    elif door_stair == "UC-C":
        pf_stair = d_nC
        ft_stair = 0

    return pf_stair, ft_stair

def airlock(door_air):

    d_n = 0.3   #Prob. of failure of unclassified door
    d_nC = 0.2  #Prob. of failure of unclassified door with Closer
    d_fd = 0.3  #Prob. of failure fire door
    d_fdC = 0.2 #Prob. of failure fire door with Closer

    if door_air == "EI60":
        pf_air = d_fd
        ft_air = 60
    elif door_air == "EI60-C":
        pf_air = d_fdC
        ft_air = 60
    elif door_air == "EI30":
        pf_air = d_fd
        ft_air = 30
    elif door_air == "EI30-C":
        pf_air = d_fdC
        ft_air = 30
    elif door_air == "UC":
        pf_air = d_n
        ft_air = 0
    elif door_air == "UC-C":
        pf_air = d_nC
        ft_air = 0

    return pf_air, ft_air

# b = Building()
# _, _, _, _, _, door_apt, door_stair, door_air, _ = b.demo()

# pf_apt, ft_apt = apt(door_apt)
# pf_stair, ft_stair = stair(door_stair)

# print("The probability of failure of the apartment door to contain a fire, given a large fire is: {} and the time until the door fails is {} minutes.".format(pf_apt, ft_apt))

# print("The probability of failure of the stair door to contain a fire, given a large fire is: {} and the time until the door fails is {} minutes.".format(pf_stair, ft_stair))

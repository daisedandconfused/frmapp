def notcall(s_alarm):
    """
    function calculating the failure probability of no awake occupant present
    to notify fire services.
    :s_alarm : boolean indicating the presence of a smokealarm
    :p : FAILURE probability of smokealarm
    :p1 : probability of an awake occupant present
    :return nocall: 1 - p1 = probability of no awake occupant present
    :s_alarm: 0 = none, 1 = domestic (from userinput)
    """
    if s_alarm == 0:
        p = 1
    elif s_alarm == 1:
        p = 0.25

    p_home = 5/7 * 14/24 + 2/7 * 17/24
    p_awakehome = 5/7 * 7/14 + 2/7 * 10/17
    p_asleephome = 1 - p_awakehome

    # someone is at home and awake/woken up
    p1 = p_home * (p_awakehome + p_asleephome * (1-p))

    nocall = 1 - p1

    return nocall

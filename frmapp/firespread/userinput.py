class Building:
    door_options = [" EI60\n", "EI60-C\n", "EI30\n", "EI30-C\n", "UC\n", "UC-C\n"]
    layout_options = [" [1] direct access\n", "[2] stair connected to lobby\n", "[3] pressurised stair connected to lobby\n", "[4] stair in connection to an airlock and lobby\n"]
    tfo_options = [" 60\n", "90\n", "120\n", "150\n", "180\n"]


    def demo(self):
        spr = eval(input('does your design have sprinklers? (1/0) \n'))
        a = eval(input('what is the floor area in m^2 of your design? \n'))
        ns = eval(input('how many storeys does your design have? \n'))
        apps = eval(input('how many apartments are there per storey? \n'))
        y = eval(input('how many years are you considering in this analysis? \n'))
        h_max = eval(input('what is the height in meters of your building design, from ground to top level floor? \n'))
        stw = eval(input('enter the stair width in meters: \n'))
        layout = eval(input('which of these 4 options describes your floor layout best?\n' + " ".join(self.layout_options)))

        if layout == 4:
            door_air = input('enter one of the following options for your airlock door: \n' + " ".join(self.door_options))
        else:
            door_air = 0

        door_apt = input('enter one of the following options for your apartment door: \n' + " ".join(self.door_options))

        if layout == 1:
            door_stair = 0
        else:
            door_stair = input('enter one of the following options for your stairwell door: \n' + " ".join(self.door_options))

        sh = eval(input('enter the spandrel height of ur facade: \n'))
        ele = eval(input('enter [0] if no fire-figthing elevator present and [1] if present: \n'))
        s_alarm = eval(input('enter [0] if no domestic smokealarm present and [1] if present: \n'))
        aba = eval(input('enter [0] if no automatic smoke detection present and [1] if present: \n'))
        fs = eval(input('enter [0] for a traditional facade and [1] for a modern one: \n'))
        glass = eval(input('enter [1] for single-paned windows, [2] for double-paned and [3] for triple paned: \n'))
        warn = eval(input('enter [0] for no warning system, [1] for a manual warning system and [2] for an automatic warning system: \n'))
        lbc = eval(input('enter from the selection how long (in min) your structure can withstand fire: \n' + " ".join(self.tfo_options)))
        # in matlab code: lbc is 30 + input * 30, check it out

        return spr, a, ns, apps, y, h_max, stw, layout, door_air, door_apt, door_stair, sh, ele, s_alarm, aba, fs, glass, warn, lbc

# b = Building()
# b.demo()


# print(spr, a, ns, y, h_max, layout, door_apt, door_stair, door_air)

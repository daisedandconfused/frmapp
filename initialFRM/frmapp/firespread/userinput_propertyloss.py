class Building:
    tfo_options = [" 60\n", "90\n", "120\n", "150\n", "180\n"]

    def demo(self):
        spr = eval(input('does your design have sprinklers? (1/0) \n'))
        a = eval(input('what is the floor area per storey in m^2 of your design? \n'))
        c0 = eval(input('what is the monetary value per m^2 of your design? \n'))
        ns = eval(input('how many storeys does your design have? \n'))
        apps = eval(input('how many apartments are there per storey? \n'))
        npa = eval(input('how many people are there in each apartment? \n'))
        y = eval(input('how many years are you considering in this analysis? \n'))
        saf = eval(input('What is your safety factor? [1/2] \n'))
        stw = eval(input('enter the stair width in meters: \n'))
        sh = eval(input('enter the spandrel height of ur facade: \n'))
        ele = eval(input('enter [0] if no fire-figthing elevator present and [1] if present: \n'))
        s_alarm = eval(input('enter [0] if no domestic smokealarm present and [1] if present: \n'))
        aba = eval(input('enter [0] if no automatic smoke detection present and [1] if present: \n'))
        fs = eval(input('enter [0] for a traditional facade and [1] for a modern one: \n'))
        glass = eval(input('enter [1] for single-paned windows, [2] for double-paned and [3] for triple paned: \n'))
        warn = eval(input('enter [0] for no warning system, [1] for a manual warning system and [2] for an automatic warning system: \n'))
        lbc = eval(input('enter from the selection how long (in min) your structure can withstand fire: \n' + " ".join(self.tfo_options)))
        # in matlab code: lbc is 30 + input * 30, check it out

        return spr, a, c0, ns, apps, npa, y, saf, stw, sh, ele, s_alarm, aba, fs, glass, warn, lbc

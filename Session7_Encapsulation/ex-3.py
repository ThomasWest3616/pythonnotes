class Machine:

    def __init__(self, power):
        self._power = power

    @property
    def power(self):
        return self._power

    
    @power.setter
    def power(self, new_power):
        if new_power == 1 and isinstance(new_power, int): 
            self._power = new_power
            print("Machine is on")
        elif new_power == 0 and isinstance(new_power, int): 
            self._power = new_power
            print("Machine is off")
        else:
            print("Value must be either 0 or 1")

    @power.deleter
    def power(self):
	    del self._power


class Printer(Machine):
    def __init__(self, print, power):
        self._print = print
        super().__init__(power)
    
    @property
    def print(self):
        return self._print

    @print.setter
    def print(self, new_print):
        self._print = new_print


class Papertray():
    def __init__(self, paper):
        self._paper = paper
    
    @property
    def paper(self):
        return self._paper

    @paper.setter
    def paper(self, new_paper):
        if new_paper <= 0 and isinstance(new_paper, int): 
            new_paper = new_paper + 100
            self._paper = new_paper
            print("Refilling paper with 100 pcs, new amount of paper is")
        else:
            print("Amount of paper remaining: ")



printer1 = Printer("This is a test print", 1)
papertray1 = Papertray(-45)
printer1.power = 0
print(printer1.power)
papertray1.paper = -45
print(papertray1.paper)
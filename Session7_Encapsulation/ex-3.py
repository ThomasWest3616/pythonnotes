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
            print("Machine is off")
        else:
            print("Value must be either 0 or 1")

    @power.deleter
    def power(self):
	    del self._power


class Papertray():
    def __init__(self, paper):
        self.paper = paper
    
    @property
    def paper(self):
        return self._paper

    @paper.setter
    def paper(self, new_paper):
        if new_paper <= 0 and isinstance(new_paper, int): 
            new_paper = +100
            self._paper = new_paper
            print("Refilling paper with 100 pcs, new amount of paper is: " + new_paper)
        else:
            print("Amount of paper remaining: " + new_paper )

    







class Printer(Machine, Papertray):
    def __init__(self, print, power, paper):
        self._print = print
        super().__init__(power)
        super().__init__(paper)
    
    @property
    def print(self):
        return self._print

    @print.setter
    def print(self, new_print):
        self._print = new_print

printer1 = Printer("hej", 1, 6)
print(printer1.paper)
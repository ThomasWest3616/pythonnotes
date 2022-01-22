# I min præsentation vil jeg starte med at forklare lidt om OOP og fokusere encapsulation og hvordan det bliver opnået via properties. 
# Jeg vil demonstrere hvordan man bruger private og public attributter i koden, samt forklare hvad der menes med private i python. 
# Derudover vil jeg demonstrere og vise hvordan man kan arbejde med properties og forklare fordele og ulemper ved properties og 
# public attributter ift. Java’s private attributter med getters og setters. 
# Derudover vil jeg også komme ind på inheritance og hvordan man definere en ny klasse uden de store ændringer til den originale.

class Robot:
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

    def introduce_self(self):
        print("My name is " + self.name) # self = this in java

# r1 = Robot()
# r1.name = "Tom"
# r1.color = "red"
# r1.weight = 30

# r2 = Robot()
# r2.name = "Hanna"
# r2.color = "blue"
# r2.weight = 40

r1 = Robot("Tom", "red", 30)
r1.can_fly = True
print(r1.can_fly)
r2 = Robot("Hanna", "blue", 40)

r1.introduce_self()
r2.introduce_self()

class Person:
    def __init__(self, name, personality, is_sitting):
        self.name = name
        self.personality = personality
        self.is_sitting = is_sitting

    def sit_down(self):
        self.is_sitting = True

    def stand_up(self):
        self.is_sitting = False

p1 = Person("Alice", "aggressive", False)
p2 = Person("Hanks", "talkative", True)

# p1 owns r2
p1.robot_owned = r2 # creates new attribute for p1
p2.robot_owned = r1

p1.robot_owned.introduce_self()
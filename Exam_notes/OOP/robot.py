class Robot:
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

    def introduce_self(self):
        print("My name is " + self.name) # this in java

# r1 = Robot()
# r1.name = "Tom"
# r1.color = "red"
# r1.weight = 30

# r2 = Robot()
# r2.name = "Hanna"
# r2.color = "blue"
# r2.weight = 40

r1 = Robot("Tom", "red", 30)
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
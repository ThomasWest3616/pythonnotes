class A:
    def __init__(self):
        self.name = 'Thomas'

    def __len__(self):
        return len(self.name)
    
    def __add__(self, other):
        return self.name + other.name

    # 2 x toString metoder python

    # Formel præsentation med repr
    def __repr__(self):
        return f'{self.__dict__}'

    # Uformel 
    def __str__(self):
        return self.name




a = A()

b = A()

a + b

print(a + b)

print(len(a))

print(len(b))

print(repr(a))

print(a)

print(str(a))


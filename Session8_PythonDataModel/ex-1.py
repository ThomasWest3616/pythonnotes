# Get item with index from list in object
class Deck:
    def __init__(self):
        self.cards = ['A', 'K', '4', '7']

    def __getitem__(self, key):
        return self.cards[key]

    def __len__(self):
        return len(self.cards)

    def __add__(self, other):
        return self.cards + other.cards

    # Formel præsentation med repr
    def __repr__(self):
        return f'{self.__dict__}'

    # Uformel 
    def __str__(self):
        return self.cards

    def __setitem__(self, key, newvalue):
        self.cards[key] = newvalue


    def __delitem__(self, key):
        del self.cards[key]


d = Deck()

c = Deck()

print(d[0])

print(len(d.cards))

print(d.cards)

print(d + c)

d.cards[0] = 'Q'

print(d.cards)

del d.cards[1]

print(d.cards)




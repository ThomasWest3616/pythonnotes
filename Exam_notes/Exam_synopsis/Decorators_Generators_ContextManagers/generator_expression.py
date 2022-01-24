
my_list = [x for x in range(0,10)] # Dette er en list coprehension
my_generator = (x for x in  range(0,10)) # Dette er en generator expression, da vi bruger () i stedet for []

print(my_list)
print(my_generator)
next(my_generator) # Giver det næste resultat i vores generator expression
next(my_generator)
next(my_generator)

for item_left in my_generator: # Vil fortsætte hvor vi slap, da vi har 3 x next, vil den starte fra 3
    print(item_left)

# next(my_generator) # Vil give fejl, da der ikke er flere items i generatoren
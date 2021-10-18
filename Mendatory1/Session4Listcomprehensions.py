# Create a list of capital letters in the english alphabet

# Create a list of capital letter from the english aplhabet, but exclude 4 with the Unicode code point of either 70, 75, 80, 85.

# Create a list of capital letter from from the english aplhabet, but exclude every second between F & O

x = [chr(i) for i in range(65,91)]
y = [chr(i) for i in range(65,91) if i not in [70,75,80,85]]
z = [chr(i) for i in range(65,91) if i not in range(70,80,2)]

print(x)
print(y)
print(z)






# From 2 lists, using a list comprehension, create a list containing: [(‘Black’, ‘s’), (‘Black’, ‘m’), (‘Black’, ‘l’), (‘Black’, ‘xl’), (‘White’, ‘s’), (‘White’, ‘m’), (‘White’, ‘l’), (‘White’, ‘xl’)]

colors = ['Black', 'White']
sizes = ['s', 'm', 'l', 'xl']

inventory = [(c,s) for c in colors for s in sizes]
print(inventory)

sold_out = [('Black', 'm'), ('White', 's')]

stock = [(c,s) for c in colors for s in sizes if (c,s) not in sold_out]
print(stock)
# Tuples are used to store multiple items in a single variable.
# A tuple is a collection which is ordered and unchangeable.

thistuple = ("apple", "banana", "cherry")
print(thistuple)

# Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.
# Tuples allow duplicate value
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
print(len(thistuple))

# One item tuple, remember the comma
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

# String, int and boolean data types
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3, True)
tuple3 = (True, False, False)
print(type(tuple2))

# The tuple() Constructor
# Using the tuple() method to make a tuple
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

# Print the second item in the tuple:
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

# Convert the tuple into a list to be able to change it:
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

# Join tuples
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)
# I min præsentation vil jeg fokusere på de fire datastrukturer i python som er List, Tuple, Set og dictionaries. 
# Jeg vil give nogle eksempler på hvordan hver datastruktur bliver implementeret, så det giver mulighed for at benytte pythons built-in functions i klasser, 
# for at interagere med disse objekter. Derefter vil jeg demonstrere hvordan list, set og dictionaries kan benyttes. 
# Jeg vil forklare hvad en decorator er, hvordan man bruger den, hvordan den er bygget op og demonstrere hvordan man kan lave sin egen. 

# The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.
mylist = ["apple", "banana", "pineapple"]
mylist2 = ["orange, kiwi"]

print(list)

mylist.insert(0, "orange") # Tager 2 parametre index og det der skal tilføjes
mylist.append("mango") # Tilføj til sidst i listen
mylist.remove("banana") # Sletter fra list med value
mylist.pop(0) # Sletter efter index
mylist.extend(mylist2) # Tilføjer list til list til sidst

print(mylist)

# Tuples
mytuple = ("thomas", "abdu", "henrik")

# Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.
# Tuples allow duplicate value
print(len(mytuple))

# Konverter til list for at manipulere med data
y = list(mytuple)
y[1] = "kiwi"
x = tuple(y)
print(x)

# Join tuples
mytuple2 = ("pernille" , "heriette", "maja")
mytuple3 = mytuple + mytuple2

print(mytuple3)

# Sets
# Set items are unordered, unchangeable, and do not allow duplicate values.
# Note: Set items are unchangeable, but you can remove items and add new items.
thisset = {"apple", "banana", "cherry"}
print(thisset)

thisset.add("pineapple") # Add to set
thisset.remove("apple") # Remove from set

print(thisset)
print("pineapple" in thisset) # Check if pineapple is in set

# Dictionaries
# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
# Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.

thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

print(thisdict["brand"]) # Vi bruger key til at finde frem til value
print(thisdict.keys()) # Bruger vi til at få alle vores keys printet ud

thisdict["SUV"] = "Ja" # Add key and value to dict
print(thisdict)

thisdict.pop("brand") # Remove from dict using key
thisdict.update({"electric" : True}) # Updates dict
thisdict.popitem() # Removes last item from dict
print(thisdict)


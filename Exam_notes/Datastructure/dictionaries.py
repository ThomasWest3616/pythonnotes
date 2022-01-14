# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
# Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(thisdict["brand"])

# String, int, boolean, and list data types:
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

# Get the value of the "model" key
print(thisdict.get("electric"))

# Get a list of the keys:
print(thisdict.keys())

# Add a new item to the original dictionary, and see that the keys list gets updated as well:
x = thisdict.keys()

print(x) #before the change

thisdict["SUV"] = True

print(x) #after the change

# Get values
print(thisdict.values())

# Get a list of the key:value pairs
print(thisdict.items())

# Check if "model" is presant in the dict
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

# Change item in the dict
thisdict["brand"] = "Mercedes"
thisdict.update({"brand" : "Audi"})


# Add item to dict
thisdict["wheels"] = 4

# Remove items with pop()
thisdict.pop("brand")


# Remove last inserted item
thisdict.popitem()
print(thisdict)

# clear() method to empty af dict
thisdict.clear()
print(thisdict)

# Delete an dict
del thisdict

# Nested dictionaries
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
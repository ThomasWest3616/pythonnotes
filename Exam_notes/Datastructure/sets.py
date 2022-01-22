# Set Items
# Set items are unordered, unchangeable, and do not allow duplicate values.
# Note: Set items are unchangeable, but you can remove items and add new items.

thisset = {"apple", "banana", "cherry"}
print(thisset)

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

# Check set
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)

# Add to set
thisset.add("pineapple")
print(thisset)

# Add Sets
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

# Add list to set
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)

# Remove from set, if "apple" does not exist it will create an error
thisset.remove("apple")
print(thisset)

# Using discard will not raise an error
thisset.discard("apple")
print(thisset)

# Remove last item using pop()
x = thisset.pop()
print(x)
print(thisset)

# clear() method empties the set
thisset.clear()
print(thisset)

# del keyword will delete the set
del thisset

# union() method returns a new set with all items from previous sets
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

# update() method inserts the items in set2 into set2
set1.update(set2)
print(set1)

# Note: Both union() and update() will exclude any duplicate items.
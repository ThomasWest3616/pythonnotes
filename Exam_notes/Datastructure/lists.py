mylist = ["thomas", "abdu", "michael", "henrik", "jens"]
print(mylist)
mylist.insert(0, "robert")
mylist.append("lars")
mylist.remove("thomas")
mylist.pop(2)
mylist2 = ["pernille", "henriette"]
mylist.extend(mylist2)
print(mylist)

for i in mylist:
    print(i)

x = 0
while x < len(mylist):
    print(mylist[x])
    x = x + 1

print(mylist[2])

print(mylist[1:3])

print(mylist[-1])

mylist[2] = "ole"

name = "pernille"

if "pernille" in mylist:
    print(f"{name} is in this list")
else:
    print(f"{name} is not in this list")

mylist.sort()
print(mylist)



numlist = [1,6,2,8,9,10]

if 2 in numlist:
    print("Number exist")

def myfunc(n):
    return abs(n - 8)

numlist.sort(key = myfunc)
print(numlist)
    


# Lists are used to store multiple items in a single variable.
# Lists are created using square brackets
thislist = ["apple", "banana", "cherry"]

# add to list
thislist.append("pineapple")
thislist.insert(0, "orange")
print(thislist)

# remove from list
# value
thislist.remove("apple")
# ID
thislist.pop(0)
print(thislist)

# Extend list
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

# Add tuple to list
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

# The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.
# It is also possible to use the list() constructor when creating a new list.
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

# Access Items
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

# Negative Indexing
#Negative indexing means start from the end
#-1 refers to the last item, -2 refers to the second last item etc.
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

# Note: The search will start at index 2 (included) and end at index 5 (not included).
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

# This example returns the items from the beginning to, but NOT including, "kiwi"
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])
print(thislist[2:])
print(thislist[-4:-1])

# Check if Item Exists
# Check if "apple" is present in the list:
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")


# Change Item Value
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

# Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon"
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:4] = ["blackcurrant", "watermelon"]
print(thislist)

# Loop Through a List
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

# Loop Through the Index Numbers
# Use the range() and len() functions to create a suitable iterable.
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

  # While loop
  thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

  # Sort the list alphabetically:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)
thislist.sort(reverse = True)
print(thislist)

# Customize Sort Function
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)
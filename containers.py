# Python Data Types

# LIST

# Mutable
# Iterable
# Square bracket


arr = [
	5,
	"name",
	True,
	{"name": "Gabi"},
	[6,7,[5,6,0]]
]

# List Methods

arr2 = [4,6,7,9,8,6,5,1]

#arr3 = [6,8,9]

#arr2.sort()
arr2.reverse()
#arr2.pop()

#arr2.append(0)
#arr2.insert(6, 1)
#arr2.extend(arr3)
#arr2.remove(1)

#arr2.clear()

print(arr2)


# TUPLE

"""
Immutable
Iterable
2 methods => .count(arg) .index(arg)
"""

tup = (6,7,8,9)

print(tup.count(7))

# DICTIONARY

myDict = {"name": "gabi", "age": 15, "school": "TCS"}
myDict2 = {"name": "coder"}

#myDict.clear()
myDict.update(myDict2)
myDict.update({"lang": "python"})

#myDict["lang"] = "JavaScript"

#myDict.pop("lang")
#myDict.popitem()

#print(myDict["church"])

#print(myDict.get("church", "church  is not a valid key"))
print(myDict)
print(len(myDict) +1)
print(myDict.keys())
#to store anything that deals with relationship
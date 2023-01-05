# imutable data types
# tuple

# mutable data types
# list,  dict, set

# Example 1
my_set = set()

#to add
#my_set.add(6)
my_set.add('4')
my_set.add(6)
my_set.add(True)

# to remove
#my_set.remove(0)

# use this instead
#my_set.discard(0)

# to add more set data as a set
#my_set.update({8, 7, 6, 5, 4, 3})

# to clear set data
#my_set.clear()

# to remove specific data
#my_set.pop()

print(my_set)

#Example 2
U = {0,  5,  6,  7,  8,  9}
setA = {5, 6, 7,  9}
setB = {9, 8, 0}
c = setA.copy()

union = setA.union(setB)
intersect = setA.intersection(setB)

subset = setA.issubset(U)
superset = U.issuperset(setB)
disjoint = setB.isdisjoint(U)

print(superset)
print(c)
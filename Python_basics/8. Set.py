"""
Set is one of the collection data types.
We create set using {}

properties : Un-ordered collection
             Un-indexed
             Un-duplicated
             Mutable

"""
###############################################################
# basic functions
a = {1, 24113, 2332, 234, 12, 234, 23}

print(type(a))
# o/p : <class 'set'>

print(a)
# o/p : {1, 24113, 2332, 23, 234, 12}       # Un-ordered output

# print(a[2])
# o/p : TypeError: 'set' object is not subscriptable    # Un-indexed

print(len(a))
# o/p : 6

###############################################################

a = {1, 24113, 2332, 234, 12, 234, 23}

a.add(2342115154)  # add one element
print(a)
# o/p: {1, 24113, 2342115154, 2332, 23, 234, 12}

a.update([8576, 4657, 45, 56])  # add multiple elements at once
print(a)
# o/p: {8576, 1, 12, 2342115154, 23, 2332, 234, 45, 24113, 4657, 56}

###############################################################
# remove functions
a = {1, 24113, 2332, 234, 12, 234, 23}

a.remove(24113)  # remove value from set
print(a)
# o/p: {1, 2332, 23, 234, 12}

a.discard(9897)  # remove value without knowing value is available in set
print(a)
# o/p: {1, 2332, 23, 234, 12}

a.pop()  # remove any random element
print(a)
# o/p: {2332, 23, 234, 12}

a.clear()
print(a)  # remove all values at a go from set
# o/p: set()

del a  # delete set
print(a)
# o/p: NameError: name 'a' is not defined

###############################################################
# using for loop with set
a = {1, 24113, 2332, 234, 12, 234, 23}

# as there is no indexing in set we can use only for each loop and not for loop with range concept

for x in a:
    print(x)

"""
o/p:
1
24113
2332
23
234
12
"""
###############################################################
# in and not in operator
a = {1, 24113, 2332, 234, 12, 234, 23}

print(2332 in a)
print(23 not in a)
print(1 not in a)

"""
o/p:
True
False
False
"""
###############################################################
# Set can only nest tuple and not list & set

a = {1, 24113, {155, 531132, 32}, 2332, 234, 12, 234, 23}
print(a)
# o/p: TypeError: unhashable type: 'set'

a = {1, 24113, [155, 531132, 32], 2332, 234, 12, 234, 23}
print(a)
# o/p: TypeError: unhashable type: 'list'

a = {1, 24113, (155, 531132, 32), 2332, 234, 12, 234, 23}
print(a)
# o/p: {(155, 531132, 32), 1, 24113, 2332, 23, 234, 12}

###############################################################
# Converting a list into set

x = [2, 32, 4325235, 45, 2, 3]
n = set(x)
print(n)
print(type(n))

"""
o/p:
{32, 2, 3, 45, 4325235}
<class 'set'>
"""
###############################################################
# Union (print all non duplicate elements)

a = {1, 34, 341, 233, 21}
b = {23, 34, 3251, 121, 32, 21}

# we have two syntax for same operation as follows
print(a.union(b))
print(a | b)

"""
o/p:
{32, 1, 34, 233, 3251, 21, 341, 23, 121}
{32, 1, 34, 233, 3251, 21, 341, 23, 121}
"""
###############################################################
# Difference (print non-common elements)

a = {1, 34, 341, 233, 21}
b = {23, 34, 3251, 121, 32, 21}

# we have two syntax for same operation as follows
print(a.difference(b))
print(a - b)
print(b.difference(a))
print(b - a)

"""
o/p:
{1, 233, 341}
{1, 233, 341}
{32, 121, 3251, 23}
{32, 121, 3251, 23}
"""
###############################################################
# Symmetric Difference (print all elements except common elements)

a = {1, 34, 341, 233, 21}
b = {23, 34, 3251, 121, 32, 21}

# we have two syntax for same operation as follows
print(a.symmetric_difference(b))
print(a ^ b)

"""
o/p:
{32, 1, 233, 3251, 341, 23, 121}
{32, 1, 233, 3251, 341, 23, 121}
"""
###############################################################
# Intersection (print all common elements)

a = {1, 34, 341, 233, 21}
b = {23, 34, 3251, 121, 32, 21}

# we have two syntax for same operation as follows
print(a.intersection(b))
print(a & b)

"""
o/p:
{34, 21}
{34, 21}
"""
###############################################################
# Common functions min, max, sum

a = {1, 34, 341, 233, 21}

print(min(a))
print(max(a))
print(sum(a))

"""
o/p:
1
341
630
"""
###############################################################

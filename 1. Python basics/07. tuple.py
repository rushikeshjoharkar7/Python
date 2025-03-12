# List can be mutable (can update/modified)
# Tuple is immutable (can't update/modified)

a = (9, 12, 234, 12, 2)

print(a)
print(type(a))

"""
o/p:
(9, 12, 234, 12, 2)
<class 'tuple'>
"""
################################################################
# check immutability of tuple
a = (9, 12, 234, 12, 2)
a[3] = 4
print(a)

"""
o/p:
TypeError: 'tuple' object does not support item assignment
"""
#################################################################
# indexing
a = (9, 12, 234, 12, 2)
print(a[1:3])

"""
o/p:
(12, 234)
"""
#################################################################
# inbuilt functions for tuple : count(),sum(),min(),max(),index(),del a,type(),len(a)
# We can't do sort,append,insert,remove,pop,reverse in tuple (after converting it in list, it is possible)

a = (9, 12, 234, 12, 2)
print(len(a))
print(a.count(2))
print(sum(a))
print(min(a))
print(max(a))
print(a.index(12))
print(type(a))
del a

"""
o/p:
5
1
269
2
234
1
<class 'tuple'>
"""
#################################################################
# Using in and not in operator in tuple

a = (9, 12, 234, 12, 2)
print(5 in a)
print(12 in a)
print(24 not in a)

"""
o/p:
False
True
True
"""
#################################################################
# we can update a value if list is nested in tuple
a = (9, 12, 234, [12, 24, 12, 212, 4, 1], 12, 2)

a[3][3] = 243153426
print(a)

"""
o/p:
(9, 12, 234, [12, 24, 12, 243153426, 4, 1], 12, 2)
"""
#################################################################
# typecasting in tuple is possible

a = tuple("Rushi")          # converting a string into a tuple
print(a)
print(type(a))

'''
o/p:
('R', 'u', 's', 'h', 'i')
<class 'tuple'>
'''
#################################################################

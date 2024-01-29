'''
There are 4 data types in python : List, Tuple, Set, Dictionary

List :
    - list follows indexing.

'''

a = [2, 32, 45, 435, 2, 3]

print(a)
# o/p: [2, 32, 45, 435, 2, 3]

print(a[3])  # print value at 3rd index in a list
# o/p: 435

print(len(a))  # print length of list

############################################################
for i in range(len(a)):  # iterate from 0 to 5
    print(i)
'''
o/p:
0
1
2
3
4
5
'''
############################################################
for i in range(len(a)):  # iterate from 0 to 5
    print(a[i])

'''
o/p:
2
32
45
435
2
3
'''
############################################################
# for each loop : each nd every element in list :

for i in a:  # iterate in all values of list a
    print(i)

"""
o/p:
2
32
45
435
2
3
"""
############################################################
# update elements in list

a[3] = 3435825
print(a)

# o/p: [2, 32, 45, 3435825, 2, 3]

############################################################
# append the list (add element at the end of list)

a.append(2347567465)
print(a)

# o/p: [2, 32, 45, 3435825, 2, 3, 2347567465]

############################################################
# insert element at required position in list

a.insert(2, 4325235)  # insert 4325235 at 2nd index
print(a)

# o/p: [2, 32, 4325235, 45, 3435825, 2, 3, 2347567465]

############################################################
# remove elements from list

a.remove(3435825)
print(a)

# o/p: [2, 32, 4325235, 45, 2, 3, 2347567465]

############################################################
# remove last element from list

a.pop()
print(a)

# o/p: [2, 32, 4325235, 45, 2, 3]

############################################################
# remove the required element using pop function

print(a.pop(2))
print(a)

'''
o/p: 
4325235
[2, 32, 45, 2, 3]
'''

############################################################
# how to remove all elements without deleting the list

a.clear()
print(a)

# o/p: []

############################################################
# reversing the list

b = [32, 2345, 234, 3, 3451, 1]
b.reverse()
print(b)

# o/p: [1, 3451, 3, 234, 2345, 32]

############################################################
# sort the list

b.sort()
print(b)

# o/p: [1, 3, 32, 234, 2345, 3451]

colors = ["orange", "green", "yellow", "blue"]
colors.sort()
print(colors)

# o/p: ['blue', 'green', 'orange', 'yellow']

############################################################
# index of list

print(b.index(3))  # printing index of element = "3"
print(colors.index("orange"))  # printing index of element = "orange"

'''
o/p:
1
2
'''
############################################################
# nested list

k = [324, 232, [234234, 2, 23], 21, 2332, 3, 3, 32]

print(k[0])  # printing element at index 0
print(k[2][1])  # printing element at index 1 of sublist available at index 2 in list

'''
o/p:
324
2
'''

############################################################
# list can have mix of all data types of elements

m = ["orange", 234, "green", "yellow", 325, "blue"]
print(m)

# o/p: ['orange', 234, 'green', 'yellow', 325, 'blue']

############################################################
# forward and backward index
m = ["orange", 234, "green", "yellow", 325, "blue"]

# serial of forward index : m = [0,1,2,3,4,5,...,len(m)-1]
# serial of backward index : m = [-(len(m)),...,-3,-2,-1]

print(m[2])  # m[2] means 3rd index from start
print(m[-2])  # m[-2] means 2nd element from last

'''
o/p:
green
325
'''

############################################################
# slicing the list

m = ["orange", 234, "green", "yellow", 325, "blue"]

print(m[1:3])  # print all elements starting from index 1 till index 2, 3 is excluded
# o/p : [234, 'green']

print(m[1:])  # print all elements starting from index 1 till last index
# o/p : [234, 'green', 'yellow', 325, 'blue']

print(m[:3])  # print all elements from first index till 2nd index, 3 is excluded
# o/p : ['orange', 234, 'green']

print(m[:])  # print all elements from first index till last element
# o/p : ['orange', 234, 'green', 'yellow', 325, 'blue']

print(m[:5:2])  # print all elements skipping each one element from first index till 4h element, 5 is excluded
# o/p : ['orange', 'green', 325]

print(m[-1:-7:-2])  # print all elements skipping each one element from last index till first element
# o/p : ['blue', 'yellow', 234]

print(m[::-1])  # reverse the list using slicing method
# o/p : ['blue', 325, 'yellow', 'green', 234, 'orange']

############################################################
# count the no. of time the element is repeated

s = [1, 2, 3, 4, 5, 65, 4, 22, 4, 33, 2, 45, 51, 5]
print(s.count(4))  # find the occurrence of "4" in list s
# o/p: 3

############################################################
# find max, min and sum

print(max(s))
print(min(s))
print(sum(s))

'''
op:
65
1
246
'''

############################################################
# find type of data type

print(type(s))
# o/p: <class 'list'>

############################################################
# delete the list

del s

############################################################
# Using in and not in operator with list

n = ["orange", 234, "green", "yellow", 325, "blue"]

print("yellow" in n)
# o/p: True

print(2323 in n)
# o/p: False

############################################################
# concatenating two lists

q = [23, 2314, 22, 234, 1]
w = [324, 23, 1, 23, 2342, 123]

e = q + w
print(e)

# o/p: [23, 2314, 22, 234, 1, 324, 23, 1, 23, 2342, 123]

############################################################
# extending one list with other

g = [324, 23, 1, 23, 2342, 123]
h = [23, 2314, 22, 234, 1]

g.extend(h)
print(g)

h.extend(g)
print(h)

'''
o/p: 
[324, 23, 1, 23, 2342, 123, 23, 2314, 22, 234, 1]
[23, 2314, 22, 234, 1, 324, 23, 1, 23, 2342, 123, 23, 2314, 22, 234, 1]
'''


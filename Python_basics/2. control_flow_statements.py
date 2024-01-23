for i in range(1, 11):
    print(i)

'''
output:
1
2
3
4
5
6
7
8
9
10
'''

###################################

for i in range(1, 11):
    if i == 5:
        break  # take outof for loop
    print(i)

'''
o/p : 
1
2
3
4
'''

###################################
for i in range(1, 11):
    if i == 5:
        continue  # skips the current iteration only
    print(i)

'''
o/p:
1
2
3
4
6
7
8
9
10

'''
###################################
i = 1

while i <= 10:
    print(i)
    i += 1

'''
o/p:
1
2
3
4
5
6
7
8
9
10
'''

###################################
i = 1

while i <= 10:
    if i == 5:
        break
    print(i)
    i += 1

'''
o/p:
1
2
3
4
'''

###################################
i = 1

while i <= 10:
    if i == 5:
        continue

    print(i)
    i += 1

'''
o/p:
1
2
3
4
'''
###################################
i = 1

while i <= 10:
    if i == 5:
        i += 1
        continue

    print(i)
    i += 1

'''
o/p:

1
2
3
4
6
7
8
9
10
'''

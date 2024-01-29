"""
Modifying Strings :
"""
#######################################################################
name = "Rushikesh joharkar"

print(name.upper())
# o/p : RUSHIKESH JOHARKAR

print(name.lower())
# o/p: rushikesh joharkar

print(name.capitalize())
# o/p : Rushikesh joharkar           # capitalize only first letter

print(name.title())
# o/p : Rushikesh Joharkar           # capitalize first letter of each word in string

print(name.count("joharkar"))
# o/p : 1                            # count how many times a word or letter is present in string

print(name.find("johar"))
# o/p: 10                           # prints index of first letter "j" in string
#######################################################################

# Use of strip to remove leading and trailing blank spaces

name = "   Rushikesh    "

print(name.strip())
# o/p: Rushikesh


#######################################################################
# replace letters

name = "Rushikesh"

print(name.replace("i","y"))
# o/p: Rushykesh


#######################################################################
# split words in sentence using specific term (e.g. space, comma, semi colon, colon)

x = "My name is Rushikesh"

print(x.split(" "))
# o/p: ['My', 'name', 'is', 'Rushikesh']

y = "My_name_is_Rushikesh"

print(y.split("_"))
# o/p: ['My', 'name', 'is', 'Rushikesh']


######################################################################
# comparison

name1 = 'rushikesh'
name2 = 'Varad'
name3 = 'Vaibhav'

print(name1.__eq__(name2))              # check if two strings are equal
print(name2 != name3)                   # check if two strings are not equal
print(name1.casefold().__eq__(name3))   # check if two strings are equal without bothering case of string


"""
o/p:
False
True
False
"""
######################################################################


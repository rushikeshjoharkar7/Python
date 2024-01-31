"""
There are 5 types of Inheritance :
1. Single
2. Multilevel
3. Hierarchical - two child classes have same parent class
4. Multiple - A child class has two parent classes, e.g. class C(A,B):
5. Hybrid - Hierarchical + Multiple
"""


###########################################################################################


# 1. Single


class A:
    a = 9

    def method_a(self):
        print("Inside method_a")


class B(A):  # Inherited only one class i.e. A in class B calling all stuff of class A
    b = 10

    def method_b(self):
        print("Inside method_b")


obj = B()  # here we can access all stuff of A and B class

print(obj.a)
print(obj.b)

obj.method_a()
obj.method_b()

"""
o/p:
9
10
Inside method_a
Inside method_b
"""


###########################################################################################

# 2. Multilevel

class A:
    a = 9


class B(A):
    b = 10


class C(B):
    c = 11


obj = C()
print(obj.a)
print(obj.b)
print(obj.c)

"""
o/p:
9
10
11
"""

###########################################################################################

# 3. Hierarchical - two child classes have same parent class


class A:
    a = 9


class B(A):
    b = 10


class C(A):
    c = 11


###########################################################################################

# 4. Multiple - A child class has two parent classes.

class A:
    a = 9


class B:
    b = 10


class C(A, B):
    c = 11


###########################################################################################

# 5. Hybrid - Hierarchical + Multiple

class A:
    a = 9


class B(A):
    b = 10


class C(A):
    c = 11


class D(B, C):
    d = 8


obj = D()
print(obj.a)
print(obj.b)
print(obj.c)
print(obj.d)

"""
o/p:
9
10
11
8
"""
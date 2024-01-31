"""
inheritance:
A child class acquiring the properties of Parent Class
"""


class A:
    a = 9

    def method_a(self):
        print("Inside method_a")


class B(A):  # calling all stuff of class A
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

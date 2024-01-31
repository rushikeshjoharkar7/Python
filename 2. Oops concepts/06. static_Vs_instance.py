"""
static : properties related to class
Static variables : wheels
Static methods:

instance : properties related to objects
Instance variables: color, price, mileage, model
Instance methods:
"""


class Bike:

    wheels = 2      # static variable

    @staticmethod
    def print_wheels():     # static method
        print(Bike.wheels)      # we can access static variable as class_name.static_variable (can't access instance stuff)

    @staticmethod
    def demo_method():
        Bike.print_wheels()     # static method can only access static stuff
        b1 = Bike("ROYAL_ENFIELD", "GT_650")    # can create a object reference to access instance stuff in static method
        b1.start_bike()

    def __init__(self, brand, model):    # instance method
        # initialize the class variables using method
        self.brand = brand      # instance variable
        self.model = model      # instance variable

    def start_bike(self):   # instance method
        print(self.brand+" bike having model as "+self.model+" has started.")
        print(Bike.wheels)      # instance method can access both static and instance stuff

    def stop_bike(self):
        print(self.brand+" bike having model as "+self.model+" has stopped.")

    def print_bike_details(self):
        print("brand of bike: "+self.brand)
        print("model of bike: "+self.model)


bike = Bike("ROYAL_ENFIELD", "GT_650")

# access instance variables and methods
print(bike.brand)
print(bike.model)
bike.start_bike()
bike.stop_bike()
bike.print_bike_details()

# access static variable and methods
print(Bike.wheels)
Bike.print_wheels()

"""
o/p:
ROYAL_ENFIELD
GT_650
ROYAL_ENFIELD bike having model as GT_650 has started.
ROYAL_ENFIELD bike having model as GT_650 has stopped.
brand of bike: ROYAL_ENFIELD
model of bike: GT_650
2
2
"""
"""
In previous python file, we use normal method as "initialization_method" to initiate the class.
For this we have a __init__ method.
In this file, we will see how this method is used.
"""


class Bike:

    def __init__(self, brand, model):   # when the class is called, this method will run with first priority
        # initialize the class variables using method
        self.brand = brand
        self.model = model

    def start_bike(self):
        print(self.brand+" bike having model as "+self.model+" has started.")

    def stop_bike(self):
        print(self.brand+" bike having model as "+self.model+" has stopped.")

    def print_bike_details(self):
        print("brand of bike: "+self.brand)
        print("model of bike: "+self.model)


bike = Bike("ROYAL_ENFIELD", "GT_650")
bike.start_bike()
bike.stop_bike()
bike.print_bike_details()

"""
o/p:
ROYAL_ENFIELD bike having model as GT_650 has started.
ROYAL_ENFIELD bike having model as GT_650 has stopped.
brand of bike: ROYAL_ENFIELD
model of bike: GT_650
"""
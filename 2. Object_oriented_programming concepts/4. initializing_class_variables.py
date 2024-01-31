

class Bike:

    def initialization_method(self, brand, model):
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


bike = Bike()
bike.initialization_method("ROYAL_ENFIELD", "GT_650")
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
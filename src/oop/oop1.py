# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class
class Vehicle:
    def init(self):
        pass

class FlightVehicle(Vehicle):
    def init(self):
        pass 

class Starship(FlightVehicle):
    def init(self):
        pass

class Airplane(FlightVehicle):
    def init(self):
        pass

class GroundVehicle(Vehicle):
    def init(self):
        pass 

class Car(GroundVehicle):
    def init(self):
        pass 

class Motorcycle(GroundVehicle):
    def init(self):
        pass 


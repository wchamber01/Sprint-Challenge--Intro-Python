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
    '''base class - Vehicle'''
    pass
class FlightVehicle(Vehicle):
    '''base class for Airplane and Starship'''
    pass
class Starship(FlightVehicle):
    '''child class'''
    pass
class Airplane(FlightVehicle):
    '''child class'''
    pass
class GroundVehicle(Vehicle):
    '''base class for Car and Motorcycle'''
    pass
class Car(GroundVehicle):
    '''child class'''
    pass
class Motorcycle(GroundVehicle):
    '''child class'''
    pass
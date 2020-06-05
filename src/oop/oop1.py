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

#Start of code

#Base class Vehicle
class Vehicle:
    pass

#Base/Parent class Vehicle
class FlightVehicle(Vehicle):
    pass

#Parent class FlightVehicle
class Airplane(FlightVehicle):
    pass

#Parent class FlightVehicle
class Starship(FlightVehicle):
    pass

# Base class Vehicle
class GroundVehicle(Vehicle):
    pass

#Base class GroundVehicle
class Car(GroundVehicle):
    pass

#Base class GroundVehicle
class Motorcycle(GroundVehicle):
    pass 
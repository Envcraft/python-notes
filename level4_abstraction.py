# Level 4 - Topic 5: Abstraction
# Hide complexity, expose only what's needed
# Use abc module for Abstract Base Classes

from abc import ABC, abstractmethod

# Abstract class - cannot be instantiated directly
class Vehicle(ABC):

    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    @abstractmethod
    def fuel_type(self):
        """Must be implemented by subclasses"""
        pass

    @abstractmethod
    def start(self):
        pass

    # Concrete method (shared by all)
    def describe(self):
        print(f"{self.brand} - {self.fuel_type()}, max {self.speed} km/h")

class ElectricCar(Vehicle):
    def fuel_type(self):
        return "Electric"

    def start(self):
        print(f"{self.brand}: Silently starting...")

class GasCar(Vehicle):
    def fuel_type(self):
        return "Gasoline"

    def start(self):
        print(f"{self.brand}: Vroom!")

# vehicle = Vehicle("Test", 100)  # TypeError: can't instantiate abstract class

tesla = ElectricCar("Tesla", 250)
bmw = GasCar("BMW", 220)

tesla.start()     # Tesla: Silently starting...
bmw.start()       # BMW: Vroom!
tesla.describe()  # Tesla - Electric, max 250 km/h
bmw.describe()    # BMW - Gasoline, max 220 km/h

# Abstraction also means using things without knowing internals
import math
print(math.sqrt(16))   # We don't know HOW it works, just WHAT it does
print(len([1, 2, 3]))  # Same idea

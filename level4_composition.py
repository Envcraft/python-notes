# Level 4 - Topic 3: Composition
# "Has-A" relationship (vs inheritance "Is-A")
# Build complex objects by combining simpler ones

class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def start(self):
        print(f"Engine ({self.horsepower}hp) started.")

    def stop(self):
        print("Engine stopped.")

class Wheels:
    def __init__(self, count):
        self.count = count

    def roll(self):
        print(f"{self.count} wheels rolling.")

# Car HAS-AN Engine and HAS Wheels (composition)
class Car:
    def __init__(self, brand, horsepower, wheel_count):
        self.brand = brand
        self.engine = Engine(horsepower)   # composed object
        self.wheels = Wheels(wheel_count)  # composed object

    def drive(self):
        self.engine.start()
        self.wheels.roll()
        print(f"{self.brand} is moving!")

    def park(self):
        self.engine.stop()
        print(f"{self.brand} is parked.")

car = Car("Toyota", 150, 4)
car.drive()
# Engine (150hp) started.
# 4 wheels rolling.
# Toyota is moving!

car.park()
# Engine stopped.
# Toyota is parked.

# Composition is preferred over inheritance when:
# - The relationship is "has-a" not "is-a"
# - You want to swap parts (e.g., different engine types)
electric_engine = Engine(300)
car.engine = electric_engine  # swap the engine!
car.drive()

from abc import ABC, abstractmethod

# Abstract Base Class
class Vehicle(ABC):
    @abstractmethod
    def number_of_wheels(self):
        pass

    @abstractmethod
    def fuel_type(self):
        pass

# Concrete Class
class Car(Vehicle):
    def number_of_wheels(self):
        return 2+2

    def fuel_type(self,fuel_type):
        return fuel_type

# Concrete Class
class Bike(Vehicle):
    def number_of_wheels(self):
        return 1+1

    def fuel_type(self):
        return "Diesel"

# Usage
car = Car()
bike = Bike()
print(f"Car: {car.number_of_wheels()} wheels, Fuel: {car.fuel_type("Petrol")}")
print(f"Bike: {bike.number_of_wheels()} wheels, Fuel: {bike.fuel_type()}")
# Output:
# Car: 4 wheels, Fuel: Petrol
# Bike: 2 wheels, Fuel: Diesel

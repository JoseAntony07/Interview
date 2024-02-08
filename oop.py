class BaseClass:
    def __init__(self):
        print("Initializing BaseClass")


class DerivedClass(BaseClass):
    def __init__(self):
        # Call the __init__ method of the base class
        super().__init__()
        print("Initializing DerivedClass")


# Creating an instance of the derived class
obj = DerivedClass()


# Abstract class

# Python program demonstrate
# abstract base class work
from abc import ABC, abstractmethod


class Car(ABC):

    @abstractmethod
    def mileage(self):
        pass


class Tesla(Car):
    def mileage(self):
        print("The mileage is 30kmph")


class Suzuki(Car):
    def mileage(self):
        print("The mileage is 25kmph ")


class Duster(Car):
    def mileage(self):
        print("The mileage is 24kmph ")


class Renault(Car):
    def mileage(self):
        print("The mileage is 27kmph ")

    # Driver code


t = Tesla()
t.mileage()

r = Renault()
r.mileage()

s = Suzuki()
s.mileage()

d = Duster()
d.mileage()

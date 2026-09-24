### Abstraction: It is concept that can hide sensitive data usng access modifiers.

from abc import ABC,abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        """hide sensitive data"""
        pass

    @abstractmethod
    def perimeter(self):
        pass 

class Circle(Shape):
    def __init__(self,radius):
        # private attribute
        self.__radius = radius 

    def area(self):
        return 3.14 * (self.__radius**2)

    def perimeter(self):
        return 2 * 3.14 * self.__radius

circle = Circle(5)
print(f"Area:{circle.area()}")
print(f"Perimeter:{circle.perimeter()}")
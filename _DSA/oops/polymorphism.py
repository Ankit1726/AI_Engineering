# Polymorphism(Method Overloading): same class --> multiple signatures
class Animal:
    def speak(self):
        print("animal makes sound")

class Dog(Animal):
    def speak(self):
        print("Dog barks: Woof..!")

class Cat(Animal):
    def speak(self):
        print("Cat meows: Meow..!")

animals = [Animal(),Dog(),Cat()]
for i in animals:
    i.speak()
print()

# ------------ Compile Time Polymorphism ------------ 
class Calculator: # function overloading 
    def add(self,a,b,c=0):
        return a+b+c 

cal = Calculator()
print(cal.add(10,20))
print(cal.add(10,20,30))
print()

# ----------- Run Time Polymorphism -----------
class Person: # function overriding 
    def getInfo(self):
        print("person class called..✅")

class Student: 
    def getInfo(self):
        print("student class called..✅")

p = Person()
p.getInfo()

s = Student()
s.getInfo()

# ----------------- Virtual Function ----------------- 
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def draw(self):
        """Pure virtual method - must be implemented by subclasses"""
        pass

class Circle(Shape):
    def draw(self):
        print("Drawing a Circle")

class Square(Shape):
    def draw(self):
        print("Drawing a Square")


c = Circle()
c.draw()  

s = Square()
s.draw() 
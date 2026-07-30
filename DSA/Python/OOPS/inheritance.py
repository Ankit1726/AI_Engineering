## INheritance
class Animal:
     def __init__(self,name):
          self.name = name 

     def eat(self):
          print(f"{self.name} is eating..!")


class Dog(Animal):
     def __init__(self, name,breed):
          super().__init__(name)
          self.breed = breed

     def bark(self):
          print(f"{self.name}, the {self.breed}, says Woof!")

     def routine(self):
        # super() can also be used to call regular parent methods
        super().eat()  
        self.bark()


my_dog = Dog("Buddy", "Golden Retriever")
print(my_dog.breed,my_dog.name)

my_dog.routine()

### Tyoes of Inheritance 

# Single Inheritance 
class Device:
    def power_on(self):
        return "Device is now ON."
class Laptop(Device):
    def browse(self):
        return "Browsing the internet..."

my_laptop = Laptop()
print(my_laptop.power_on()) 
print(my_laptop.browse())   

# Multi-Level Inheritance 
class Grandfather:
    def land(self):
        return "A beautiful farmland."

class Father(Grandfather):
    def house(self):
        return "A 3-bedroom apartment."

class Son(Father):
    def car(self):
        return "A modern electric car."

junior = Son()
print(junior.land())
print(junior.house())
print(junior.car())  

# Multiplle Inheritance 
class Father:
    def business_skills(self):
        return "Excellent marketing skills."

class Mother:
    def artistic_skills(self):
        return "Beautiful painting skills."

# Child inherits from BOTH classes separated by a comma
class Child(Father, Mother):
    def play(self):
        return "Playing video games."

kid = Child()
print(kid.business_skills()) # From Father
print(kid.artistic_skills()) # From Mother

# Hierarchial Inheritance 
class Vehicle:
    def fuel_type(self):
        return "Requires energy to run."

# Child Class 1 (Sibling A)
class Car(Vehicle):
    def drive(self):
        return "Driving on four wheels."

# Child Class 2 (Sibling B)
class Bike(Vehicle):
    def ride(self):
        return "Riding on two wheels."
    
my_car = Car()
my_bike = Bike()

print(my_car.fuel_type())
print(my_bike.fuel_type())

# Hybrid Inheritance 
class SchoolMember:
    def __init__(self, name):
        self.name = name
        
    def introduce(self):
        return f"Hi, my name is {self.name}."

class Teacher(SchoolMember):
    def teach(self):
        return "I am teaching a lesson."

class Student(SchoolMember):
    def study(self):
        return "I am studying for exams."

class TeachingAssistant(Teacher, Student):
    def grade_papers(self):
        return "I am grading assignments."

T = TeachingAssistant("Alex")
print(T.introduce())
print(T.teach())
print(T.study())
print(T.grade_papers())
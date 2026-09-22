### Inheritance(Method Overriding): (Base Class --> Parent Class)
class Person:
    def __init__(self, name, age):  # parent class
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name:{self.name}")
        print(f" Age:{self.age}")


class Student(Person):
    def __init__(self, name, age, roll_num):
        super().__init__(name, age)
        self.roll_num = roll_num

    def display_info(self):
        super().display_info()
        print(f"Roll No:{self.roll_num}")


s1 = Student("Ankit", 22, 107)
s1.display_info()


##------------  Types of Inheritance --------------
# Single Inheritance
class Animal:
    def eat(self):
        print("Eating...")


class Dog(Animal):
    def bark(self):
        print("Barking...")


d = Dog()
d.eat()
d.bark()


# Multi-level Inheritance
class Grandparent:
    def house(self):
        print("Grandparent's House")


class Parent(Grandparent):
    def car(self):
        print("Parent's Car")


class Child(Parent):
    def bike(self):
        print("Child's Bike")


c = Child()
c.house()
c.car()
c.bike()


# Multiple Inheritance
class Father:
    def gardening_skill(self):
        print("Loves Gardening")


class Mother:
    def cooking_skill(self):
        print("Loves Cooking")


class Child(Father, Mother):
    def coding_skill(self):
        print("Loves Coding")


c = Child()
c.gardening_skill()
c.cooking_skill()
c.coding_skill()


# Multiple Inheritance
class Parent:
    def property(self):
        print("Parent's Property")


class Child1(Parent):
    def play_cricket(self):
        print("Child 1 plays Cricket")


class Child2(Parent):
    def play_football(self):
        print("Child 2 plays Football")


c1 = Child1()
c2 = Child2()

c1.property()
c2.property()


# Hybrid Inheritance
class School:
    def school_name(self):
        print("ABC Public School")


class Student1(School):  # Hierarchical part
    def student1_info(self):
        print("Student 1")


class Student2(School):  # Hierarchical part
    def student2_info(self):
        print("Student 2")


class SportsCaptain(Student1, School):  # Multiple part
    def captain_info(self):
        print("Sports Captain")


sc = SportsCaptain()
sc.school_name()
sc.student1_info()
sc.captain_info()
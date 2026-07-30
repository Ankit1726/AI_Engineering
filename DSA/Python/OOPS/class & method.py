 ## Class & Method 
class Person:
     # constructor 
     def __init__(self,name,age):
          self.name = name  # attributes
          self.age = age

p = Person("Ankit",21)
print(p.name,p.age)

### Methods Types 
# instance method(belongs to specific object)
class Student:
     def __init__(self,name,branch):
          self.name = name  # instance variable
          self.branch = branch

     # Instance Method 
     def introduce(self):
          return f"I am {self.name} & pursuing branch {self.branch}"
     

s1 = Student("Ankit","AIML")
print(s1.introduce())

# class method(belongs to entore class itself)
class Insan:
     species = "Human"
     @classmethod
     def change_species(cls,new_species):
          cls.species = new_species

Insan.change_species("Homo Sepians")

i1 = Insan()
print(i1.species)

# static method(isolated to others)
class Age:
     @staticmethod
     def is_adult(age):
          return age>=18

a = Age()
print(a.is_adult(20))

## Method Overloading 
class Calci:
     def add(self,a,b):
          return a+b # Ignore completely

     def add(self,a,b,c):
          return a+b+c # ✅

     def add(self,a,b,c,d=0): # Implicit Overloading
          return a+b+c+d

c = Calci()
print(c.add(23,9,12))
print(c.add(21,23,44,55))

## Method Overriding 
class Cal:
     def add(self,a,b):
          return a+b

class Calci(Cal):
     def add(self, a, b,c=0):
          return super().add(a, b)+c

calculator = Calci()
print(calculator.add(32,45))
print(calculator.add(4,5,6))
## Public Access Modiifer
class Employee:
     def __init__(self,name):
          self.name = name

emp = Employee("Ankit")
print(emp.name)

## Protected Access Modifier
class Parent:
     def __init__(self):
          self._project = "Secret Bluprint"

class Child(Parent):
     def show_project(self):
          print(self._project)

c = Child()
c.show_project()

## Provate Access Modifier
class Person:
     def __init__(self,salary):
          self.__salary = salary # provate variable

     def __calculateSal(self):
          return self.__salary

p = Person(99434)
print(p._Person__salary) # name mangling used this to access private variable
## Aggregation Relationship (independfent eachother)
class Car:
     def __init__(self,brand,color):
          self.brand = brand 
          self.color = color

class Person:
     def __init__(self,name,car):
          self.name = name 
          self.car = car

     def show_details(self):
          return f"{self.name} owns a {self.car.color} {self.car.brand}."

my_car = Car("GWagon","black")
owner = Person("Ankit",my_car)
print(owner.show_details())

## Composition Relationship 

class Engine:
     def engine_details(self):
          print("engine name TR343_Turbo")

class Tyre:
     def tyre_details(self):
          print("4 tyre car")

class Door:
     def door_details(self):
          print("automatic sensor doors")

class Car:
     def __init__(self):
          self.engine = Engine()
          self.tyre = Tyre()
          self.door = Door()

     def print_details(self):
          self.engine.engine_details()
          self.tyre.tyre_details()
          self.door.door_details()

c = Car()
c.print_details()
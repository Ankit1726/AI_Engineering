## Polymorphism Implementation
class Animal:
     def eat(self):
          return "Animal is eating..!"

class Dog(Animal):
     def eat(self):
          return "Dog is eating..!"

class Cat(Animal):
     def eat(self):
          return "Cat is eating..!"

d = Dog()
c = Cat()
a = Animal()

print(a.eat())
print(d.eat())
print(c.eat())

## Duck Typing Concept
class BirdFly:
     def flybird(self,bird):
          bird.fly()

class Parrot:
     def fly(self):
          return "Parrot is Fly..!"

class Crow:
     def fly(self):
          return "Crow is Fly..!"

p = Parrot()
c = Crow()

print(c.fly())
print(p.fly())
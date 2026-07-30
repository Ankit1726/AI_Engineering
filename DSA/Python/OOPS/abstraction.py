## Abstraction
from abc import ABC,abstractmethod

class Animal(ABC):
     @abstractmethod
     def eat(self):
          pass

class Dog(Animal):
     def sleep(self):
          return "Dog is sleeping..!"
     def eat(self):
          return "Dog is eating..!"

dog = Dog()
print(dog.sleep())
print(dog.eat())
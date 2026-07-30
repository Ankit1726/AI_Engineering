## Encapsulation (wrapping up {data+method} into single object)
class Car:
     def __init__(self,name):
          self.__name = name # provate variable

     # Getter & Setter {public method to access private data}
     def get_name(self):
          return self.__name

     def set_name(self,new_name):
          self.__name = new_name

c = Car("Mercedies GWagon")
print(c.get_name())
c.set_name("BMW 77")
print(c.get_name())


## Mini Bank System 
class BankAccount:
     def __init__(self,owner,bal):
          self.owner = owner
          self.__bal = bal

     # Getter Method 
     def get_bal(self):
          return self.__bal

     # Setter Method 
     def deposit(self,amount):
          if amount > 0:
               self.__bal+=amount 
               print(f"Deposited {amount} & New Balance:{self.__bal}")
          else:
               print(f"Invalid deposit amount")
customer = BankAccount("Ankit",995790)
print(customer.owner)
print(customer.get_bal())
print(customer.deposit(67574))
print(customer.get_bal())
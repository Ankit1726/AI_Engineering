### Access Modifiers {Public,Protected & Private}
class Person:
    def __init__(self,name,age):
        self.name = name # public attribute
        self._age = age  # protected attribute 

    def greet_name(self):
        print(f"Hello {self.name}..👋")

    def show_age(self):
        print(f"{self.name}'s age is {self._age} years.")

obj = Person("Alexa",21)
obj.greet_name()
obj.show_age()

class BankAcc:
    def __init__(self,bal,amount):
        # private attribute
        self.__bal = bal 
        self.__amount = amount

    def get_bal(self): # access by getter method 
        return self.__bal

    def deposit_money(self,amount): # set by setter method
        self.__bal+=amount
        return "deposited sucess✅"

account = BankAcc(1430332,0)
print(f"account balance:{account.get_bal()}$")
account.deposit_money(33343532)
print(f"account balance:{account.get_bal()}$")
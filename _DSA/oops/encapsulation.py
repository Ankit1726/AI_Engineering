# Encapsulation: It is the process of bundling data (variables) and the methods (functions) that operate on that data into a single unit (a class).

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner          # Public attribute
        self._account_type = "Savings" # Protected attribute (convention)
        self.__balance = balance    # Private attribute (hidden)

    # Getter method to read private data safely
    def get_balance(self):
        return self.__balance

    # Setter method to modify private data with validation
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited Rs.{amount}. New Balance: Rs. {self.__balance}")
        else:
            print("Invalid deposit amount!")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew Rs.{amount}. Remaining Balance: Rs. {self.__balance}")
        else:
            print("Insufficient funds or invalid amount!")

account = BankAccount("Ankit", 435400)

print("Account Owner:", account.owner)

# Accessing Private Member directly will fail:
# print(account.__balance)  # AttributeError

print("Initial Balance:", account.get_balance())  
account.deposit(5054330)                             
account.withdraw(20000)                            
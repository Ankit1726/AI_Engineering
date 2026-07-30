# Exception Handling 
def add(a,b):
     try:
          return a/b
     except Exception as e:
          print(type(e).__name__)
          print(e)
     finally:
          print("task completed..✅")

# raise exception 
def check_age(age):
    try:
        if age < 0:
            raise ValueError("Age cannot be a negative number.")
            
        elif age > 140:
            raise ValueError("This is not a realistic age (cannot be greater than 140).")
        else:
            return f"Age {age} is valid and accepted."
            
    except ValueError as e:
        return f"Invalid Input Error: {e}"

# Custom Exception
class InsufficientFundsError(Exception):
    pass

def withdraw_money(balance, withdraw_amount):
    if withdraw_amount > balance:
        raise InsufficientFundsError("Not enough balance")
    print(f"Remaning balance = {balance-withdraw_amount}")

try:
    withdraw_money(10000, 5000)
except InsufficientFundsError as e:
    print(f"Error name :{type(e).__name__}")
    print(f"error :{e}")
except Exception as e:
    print(f"Error name :{type(e).__name__}")
    print(f"error :{e}")
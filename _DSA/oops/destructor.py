## Destructor Class 
class Student:
    def __init__(self,name):
        self.name = name 
        print(f"Constructor:{self.name} makes success✅")

    def __del__(self):
        print(f"Destructor:{self.name} deallocate successfully✅")

obj = Student("Ankit")
del obj
# Static Keyword (universal variable shared among all classes)

class Student:
    school_name = "Indus AI School" # static variable
    def __init__(self,name,roll_no):
        self.name = name 
        self.roll_no = roll_no

    @staticmethod
    def is_valid(age):
        """Utility method: doesn't need access to self or school_name"""
        return age >= 5

print(f"School Name:{Student.school_name}")
print(f"Is Elgible:{Student.is_valid(7)}")
s1 = Student("Ankit",101)
s2 = Student("kavi",102)

Student.school_name = "Indus World's Of Technology"
print(s1.school_name)
print(s2.school_name)
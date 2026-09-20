# class 
class Car:
    def __init__(self,brand,color):
        # attributes
        self.color = color
        self.brand = brand 

    # method (behaviour)
    def specifications(self):
        print(f"Car Brand:{self.brand} & Car Color:{self.color}")

# create object 
c1 = Car("Toyata","Red")
c1.specifications()
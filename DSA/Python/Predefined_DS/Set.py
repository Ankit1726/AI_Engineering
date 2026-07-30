## Set 
my_set = {1,2,3,4,5}
print(my_set)
print(type(my_set))
print(len(my_set))

# method 
s = {10, 20, 30}
s.add(40) 
print(s)
s.remove(10)
print(s)
print(s.pop()) 
s.clear()
print(s) 

# Union & Intersection
A = {1, 2, 3}
B = {3, 4, 5}
print(A.union(B)) # {1, 2, 3, 4, 5}
print(A.intersection(B)) # {3}
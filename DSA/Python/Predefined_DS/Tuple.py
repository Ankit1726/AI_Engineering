## Tuple 
tup = (10,20,30,40)
print(tup)
print(type(tup))

# Single Tuple
single_tup = (34,)
print(single_tup)

# Indexing & Slicing 
t = (10, 20, 30, 40)
print(t[0]) # 10
print(t[-1]) # 40
print(t[1:3]) # (20, 30)

# Looping on Tuple 
for i in t:
     print(i,end=" ")
print()

# Tuple Methods
tu = (1,2,1,2,3,4,5,6,2,3,1,2,2)
print(tu.index(2))
print(tu.count(2))

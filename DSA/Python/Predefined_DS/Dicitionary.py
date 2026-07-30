## Dictionary 
my_dict = {
     "name":"Ankit Gupta",
     "age":22,
     "profession":"AI Engineer"
}
print(my_dict)
print(type(my_dict))

# Methods 
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())
print(my_dict.get("profession"))
new_item = {"city":"Noida"}
print(my_dict.update(new_item))
print(my_dict)

# Loop on dictionary
for k,v in my_dict.items():
     print(k,v)
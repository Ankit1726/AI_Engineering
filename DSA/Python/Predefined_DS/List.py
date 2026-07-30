## List 
my_list=["apple",1,2,3]
print(my_list)
print(type(my_list))

# Access List Element 
lst = ['apple','cherry','banana']
print(lst[0])
print(lst[-1])
print(lst[::-1])

lst[2] = "watermelon"
print(lst)

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(len(nums))

nums.append(10)
print(nums)

nums.insert(1,4)
print(nums)

nums.reverse()
print(nums)

# Loop on List 
num = [1,2,4,3,2,5]
for i in num:
     print(i,end=" ")

# Linear Search 
def linear_search(num,x):
     idx = 0
     for i in num:
          if(num == x):
               print(f"{x} found at index:{idx}")
               break
          idx+=1

# Enumerate Function
def my_enumerate(ar):
     for i,v in enumerate(ar):
          if(v%2==0):
               print(i,end=" ")

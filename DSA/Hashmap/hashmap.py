# Creating Hashmap
from collections import defaultdict,Counter

grades = {
     "Ankit":99,
     "Kush":78,
     "Kaveri":80
}

# Inserting Grades 
grades["David"] = 75  
grades["Alice"] = 98

# Delete Item
del grades["David"]
print(f"student grades: {grades}")
print(type(grades))

# Iterating Hashmap
print("Student Record\n")
for name,grade in grades.items():
     print(f"{name}:{grade}")

# Default Dictionary 
freq = defaultdict(int)
for ch in "banana":
    freq[ch] += 1
print(freq)

# Counter 
nums = [1,2,2,3,3,3]
print(Counter(nums))
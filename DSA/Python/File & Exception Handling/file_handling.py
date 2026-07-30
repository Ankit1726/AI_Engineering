# Read entire file in single string 
f = open("file.txt","r") 
content = f.read()
f.close()

# Read one line at a time 
f = open("file.txt","r")
l1 = f.readline()
l2 = f.readline()
f.close()

# Create new file if not exist
f = open("greet.txt","x")
f.writelines(["Hello Everyone\n","Myself Ankit Gupta as Lead AIML Engineer..!"])
f.close()

# Write into File 
f = open("greet.txt","w")
f.write("Hello Evdryone I am Ankit Gupta as Senior Lead Engineer at google..!how are you all")
f.close

# Recommended Appraoch Using With Context Manager
with open("file.txt","r") as f:
     content = f.read()
     print(content)

# deleting exisiting file 
import os 
os.remove("greet.txt")
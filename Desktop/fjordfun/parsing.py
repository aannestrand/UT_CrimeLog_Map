import re

with open('output.txt', 'r') as f:
    lines = f.readlines()

count = 0;

for line in lines:
    
    parts = line.split(" ")
    if(re.search("[0-9]", parts[0]) and not(re.search("/", parts[0])) and (len(parts) >= 2) and not(re.search("[a-z]", parts[0]))): 
        print(line)
        count += 1
        
print(x)
    
    



'''line = "a5b3c2"
out=""
for i in line:
    if i.isalpha():
        x = i
    else:
        d = int(x)
        out = out + x *d
print(out)'''

import csv

path = "F:\GS.csv"
file = open(path,newline=" ")
reader = csv.reader(file)
new = next(reader)
data = [row for row in reader]
print(data)
print(new)
        
        

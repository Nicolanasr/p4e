import re
fhandle = open('Actual data.txt')
numlist = list()

sum = 0

for line in fhandle:
    stuff = re.findall('[0-9]+', line)
    if len(stuff) > 0:
        numlist.append(stuff)

for i in numlist:
    for j in i:
        sum = sum + int(j)

print(sum)
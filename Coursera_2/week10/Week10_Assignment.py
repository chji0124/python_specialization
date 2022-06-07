name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"

fileHandler = open(name)

counts = dict()
lst = list()

for line in fileHandler:
    if not line.startswith("From "): continue
    words = line.split()
    lst.append(words[5])

lst.sort()
    
listOfHours = list()    
for word in lst:
    hours = word.split(':')
    listOfHours.append(hours[0])
    
    
print(listOfHours)
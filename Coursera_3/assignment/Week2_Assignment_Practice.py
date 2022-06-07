import re 

fileHandler = open('/Users/jamie/Desktop/regex_sum_1451275.txt') # opening a file

numbers = list() #creating an empty list
Sum = 0

for line in fileHandler: # using for loops to iterate over a sequence
    line = line.rstrip() #stripping white spaces on the right handside
    nums = re.findall('[0-9]+',line) #to extract matching string for one or more digits 
    numbers.append(nums)
    #print(numbers)

for n in numbers: #used for loop to get sum of the numbers
    Sum = Sum + int(n)

print(Sum)
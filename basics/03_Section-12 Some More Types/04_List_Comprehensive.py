'''
    Comprehensive method
    variable = [
    expression
    for iteration_variable in list/identifier/variable
    if condition
    ]
'''

# Normal method to split string to individual character
result=[ ]
for i in "inmakes":
    result.append(i)
print(result)

# Comprehensive method to split string to individual character
result=[i for i in  "inmakes"]
print(result)

# Normal method to find out string start with 'p'
result=["python","django", "flask", "people"]
new=[ ]
for i in result:
    if 'p' in i:
        new.append(i)
print(new)

#Comprehensive method  to find out string start with 'p'
new = [i for i in result if 'p' in i ]
print (new)

#Comprehensive method  to print 0 to 10
new = [i for i in range(10)]
print (new)

#Comprehensive method  to replace list content with Markz
list1 = [1,2,3,4,5]
new = ["Markz"  for i in list1]
print(new)

#Comprehensive method  to print the lower case list item to upper case
result=["python","django", "flask", "people"]
new = [i.upper() for i in result]
print(new)

#Comprehensive method  to multiply the list of number with same number
num=[1,4,6,7]
new = [i*i for i in num]
print (new)
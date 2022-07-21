#create tuple
x=(12,13, "hello","python")

#print the type of x
print(type(x))

#print the 0th element in x
print(x[0])

"""Tuple not allow to add and remove elements then we convert the tuple into list
 and add or remove from it. after we re-convert to tuple"""

y=list(x)
print(y)
print(type(y))
y.insert(2, "hello1")
print(y)
x=tuple(y)
print((x))

#length of the tuple
print(len(x))

#Create tuple using construct method
z=tuple(("pp","jj","hh"))
print(z)

#list the tuple items using loop
for x1 in z:
    print(x1)

#concatnation of two tuples y and z
y= (1,2,3,5)
print(z+y)

#Replication the tuple n time (n=3)
y= x*3
print(y)

import pydoc

def addition(a,b):
    '''function for add two numbers'''
    return a+b

def square (c):
    '''function to find out the square of a number '''
    return c*c

result=square(addition(2,3))
print(result)
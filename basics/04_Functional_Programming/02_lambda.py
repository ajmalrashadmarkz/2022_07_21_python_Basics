import pydoc
'''
 lambda arguments :expression
 lambda:keyword 
'''
x=lambda a,b :a+b
''' 
    X(arguments) passed to lambda function & result passed to print 
'''
print(x(2,3))

x=lambda a:a+30
''' 
 Only passed one arguments to lambda 
'''
print(x(7))

x=lambda a,b,c :a+30+b*c
''' 
 In this case multiple  arguments to lambda function 
'''
print(x(7,7,4))

def fun(n):
    return lambda b:b+n
x=fun(2)
'''passed argument value for function like 2'''
print(x(8))
'''passed argument value for lambda like 8'''


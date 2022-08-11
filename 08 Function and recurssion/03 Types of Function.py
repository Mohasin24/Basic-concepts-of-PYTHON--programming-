# 01: Built in function:- already defined/present in python
#Examples:- print(), len(), range(), etc.

# 02: User defined function:-the function which are defined by users
#Example :-
def greet(name):
    print (('Good Day, ' + name + '.'))

greet(input('Enter Your Name:\n').capitalize())

#Here greet() is a user defined function

def mysum(num1, num2):
    return num1+num2

s = mysum(55,58)    
print(s)

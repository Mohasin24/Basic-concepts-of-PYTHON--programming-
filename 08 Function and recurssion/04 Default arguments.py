# Default Argument:
'''
We can have a value as a default argument in a function.
If we specify name='Stranger' in the line containing def, this value is 
used when no argument is passed.
'''

#Example :

def greet(name='Stranger'):
    print (('Good Day, ' + name + '.'))

greet(input('Enter Your Name:\n').capitalize())
greet() #Here we do not passed any argument then it will take stranger as a default argument


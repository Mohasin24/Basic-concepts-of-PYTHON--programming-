#Function with argument:
'''
A function can accept some values it can work with. We can put these values in the 
paranthesis. A function can also return values as shown below:
'''

def greet(name):
    gr = 'Hello ' + name
    return gr
a = greet('Mohasin') # Here 'Mohasin' is passed to greet to 'name'   
print(a)
def myfunc() : #Arithmetic operators
 x = 20
 y = 10

 # Arithmetic operators
 '''arithmetic operators are mathematical operators
 use to perform mathematical operations'''
 # e.g. '+, -, /, *' are the arithmetic operators

 print(x + y) #Addition

 print(x - y) #Subtraction

 print(x / y) #Division

 print(x * y) #Multiplication

 print(x%y)   #Remainder

 print(x//y)  #Floor Division

 print(x**y)  #Y to the power X

myfunc()

def myfunc(): #Assignment operators

    #assignment operators are '=', '+=', '/=', '*='

    a = 5
    b = 10
    c = 15
    d = 20

    #example
    
    a += 5 #it will add 5 in a
    b -= 5 #it will sub 5 in b
    c *= 5 #it will multi 5 in c 
    d /= 5 #it will div 5 in d 
    
    print ("The value of 'a += 5' is",a)
    print ("The value of 'b -= 5' is",b)
    print ("The value of 'c *= 5' is",c)
    print ("The value of 'd /= 5' is",d)
myfunc()    

def myfunc(): #comparison operators

    '''comparison operators basically compares the two 
    entities and tells us that the value of this is 
    True or False i.e. it uses booleans'''    

    """ != not equal, == equals, > greater than, 
    < less than, >= greater than equals, <=less than equals"""

    a = (7==7)
    b = (7>14)
    c = (7<14)
    d = (7!=7)

    print (a)
    print (b)
    print (c)
    print (d)
myfunc()

def myfunc() : #Logical operators
    
    ''' 'And' gives true when both the variables are true if any 
    of variable is false then it will give false'''
    # 'Or' gives true if any/both value from two variables are true and false in all other cases
    # 'not' makes true value false and false value true basically it converts

    bool1 = True
    bool2 = False
    print ('''the value of "bool1 'and' bool2" is''', (bool1 and bool2))
    print ('''the value of "bool1 'or' bool2" is''', (bool1 or bool2))
    print ('''the value of "'not' bool2" is''', (not bool2))
myfunc()

def myfunc() : #Input
    '''Input func. is used to take input from user'''
    a = (input("write your name here "))
    a = a.upper()
    print(a)
    print(type(a))

    '''the output of the input function is always a string
    even if you entered a no. it shows str in terminal
    you can use typecasting to change its data type'''
myfunc()    

def myfunc(): # % Modulus
    #if we divide two number it will give us the remainder of this two number
    x = 10
    y = 4
    print ('The remainder when x is divided by y is ',x%y)

myfunc()

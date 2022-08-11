def DataTypes():
    x = 'mohasin' #here x is a variable with data type of str

    y = 10 #here y is a variable with data type of int

    z = 10.10 #here z is a variable with data type of float

    a = True #here a is a variable with data type of boolean which gives values either true or false

    b = None #here b is a variable with data type of none

    #if you want to know the type of variable then

    print(type(x),"\n//////")

    print(type(y),"\n//////")
 
    print(type(z),"\n//////")

    print(type(a),"\n//////")

    print(type(b),"\n//////")

    '''
    variable names can only start with underscore and alphabates but not with number although it can contains no. & also we cannot add white spaces in variable names
    
    '''

    #example

    _x = 5

    x_5 = 8
    # but not '8x, 8 x, x_ 8' like this

DataTypes()    
    

def Typecasting(): #Typecasting
    
 #you can convert one data type into another by using typecasting

 #example :-

 a = 8 #here a is a int
 print(type(a))
 a = str(a) #now a is converted into str

 print ("Now 'a' became a String", a)
 print(type(a))

Typecasting()



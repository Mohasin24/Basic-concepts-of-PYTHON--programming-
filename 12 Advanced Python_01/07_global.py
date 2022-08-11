'''
"global" keyword  is used to modify the variable outside the current scope
'''
a  = 50 #Global variable

def func1():
    global a 
    print(a)
    a = 10 #local varible limited to function, now it will changes 'a=50 to a=10'
    print(a)

func1()
print(a,',after change')

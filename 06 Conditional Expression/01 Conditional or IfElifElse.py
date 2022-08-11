# 01_ If-elif-else in python:- if elif else are multiway decison taken by our program due to certain condition in our code

a = 10
# 01_This a if-elif-else ladder
if (a<5):
    print('The value of a is less than 5')
elif(a<15) :
    print('The value of a is less than 15')
else :
    print('The value of a is 10 ')        

# 02_Multiple if statements

if (a>5):
    print('The value of a is greater than 5')
if (a>6):
    print('The value of a is greater than 6')
if (a>7):
    print('The value of a is greater than 7')
elif(a<15) :
    print('The value of a is less than 15')
else :
    print('The value of a is 10 ')     

''''
 We can use multiple 'elif' statements after 'if' statement followed by 'else' statement
 This ladder will stop once a condition in an 'if' or 'elif' is met
 'else' only get exicuted if all the statements inside 'elif' fails
 'else' is optional
'''
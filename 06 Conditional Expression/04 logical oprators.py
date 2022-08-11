# Logical operators
'''
1> And:- True if both operands are true else false
2> Or :- True if at least one oprand is true in all other cases false
3> Not:- Inverts True to False & False to True  

'''
a = int(input('Enter your age:\n'))

if (a>=35 and a<=56 ):
    print('You are eligible')
else:
    print('You are not eligible')

if (a==35 or a>=35):
         print('You are eligible second case')
else:
    print('You are not eligible second case')

if (not a>=35):
    print('You are eligible third case')
else:
    print('You are not eligible third case')


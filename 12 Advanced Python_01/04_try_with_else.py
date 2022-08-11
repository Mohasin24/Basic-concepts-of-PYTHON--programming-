#Try with else:-
'''
here 'else' will only get executed if 'try' was successful
'''

try:
    a = int(input('Enter a number:\n'))
    print('Result:-')
    c = 1/a
    print(c)
except Exception as e:
    print(f'Error occured!\n{e}')
else:
    print('We are successful')   

         

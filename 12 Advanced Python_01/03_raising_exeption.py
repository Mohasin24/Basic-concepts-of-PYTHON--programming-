'''
we can raise custom exception using "raise" keyword in python
'''


while (True):
    def increment(num):
        try:
            return int(num) + 1
        except:
            raise ValueError('This is not expected value! Hello coder, please resolve this')
        
    print('Enter Q to quit')
    a = input('Enter a number:\n')
    if a=='Q' or a == 'q':
        print('Exited')
        break
    else:
        print(increment(a))
print('Thanks for using the code!')         
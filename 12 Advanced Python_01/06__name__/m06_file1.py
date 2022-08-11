def greet(name):
    print(f'Good morning, {name.upper()}.')

# print(__name__)    

if __name__=='__main__':
    n = input('Enter your name :-\n')
    greet(n)    

'''  __name__evalute to the name of the module in python from where the program is run.
    If the module is being run directly from the command line , the __name__ is set to the
string "__main__" '''
        
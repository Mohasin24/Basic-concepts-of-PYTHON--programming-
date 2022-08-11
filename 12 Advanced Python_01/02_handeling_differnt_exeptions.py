a=None

while (True):

    print('Enter q to quit!')

    a=input('Enter a number:\n')
    

    if (a=='q' or a=='Q'):

        print('Exited')
        break    
    else: 
        try:
            print('*****')
            a=int(a)
            c = 1/a 
            print(c)

        # except ValueError as e:
        #     print('Exeption1 has occured! Please enter a valid value')
        #     print(e,'\n -------') 

        except ZeroDivisionError as e: #occurs when divided by zero
            print('Make sure you did not entered zero')
            print(e,'\n -------') 

        except :
            print('Error has occured!\n*****')
                

print('Thanks for using this code.\n******')       


while(True):
    print('Enter q to exit')
    a=(input('Enter the first number:-\n'))
    
    if (a=='q' or a=='Q'):
        
        print('Exited!')
        break
    else:
        b=(input('Enter the second number:-\n'))

        if (b=='q' or b=='Q'):
            print('Exited!')
            break
        else:
            try:
                a=int(a)
                b=int(b)
                print(a/b,'\n********')
            except ZeroDivisionError:
                print('Infinite, You divided "a" by zero.\n********') 
                  
num = int(input('Enter a number:\n'))
if (num<=0):
        print('Please enter value greater than zero. ')
else:    
    prime = True

    for i in range(2, num): 
        if(num%i==0):
            prime = False
            break
    if prime:
        print('This number is a prime number.')
    else:
        print('This number is not a prime number.')        

    
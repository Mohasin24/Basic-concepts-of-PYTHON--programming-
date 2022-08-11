#02_ Takes something returns nothing
def sum(n1,n2):
   
    result = n1+n2
    
    print('Please enter two numbers')
    n1 = int(input('Enter 1st Num:'))
    n2 = int(input('Enter 2nd Num:'))
    
    sum(n1,n2) 
    print(result)
    sum(n1,n2)    
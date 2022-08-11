

def greatest(num1,num2,num3):
    if num1>num2:
        if (num1>num3):
            return num1
        else:
            return num3
    else:
       if (num2>num3):
            return num2
       else:
            return num3

num1 = int(input('Enter 1st number: \n'))
num2 = int(input('Enter 2nd number: \n'))
num3 = int(input('Enter 3rd number: \n')) 
              
print('The greatest numeber is:-',greatest(num1,num2,num3))              
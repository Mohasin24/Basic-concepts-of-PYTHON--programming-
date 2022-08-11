# Que :- Write a program to find the greatest of four numbers entered by the user

num1 = int(input('Enter 1st number: \n'))
num2 = int(input('Enter 2nd number: \n'))
num3 = int(input('Enter 3rd number: \n')) 
num4 = int(input('Enter 4th number: \n'))


if (num1>num4):
    f1 = num1
else:
    f1 = num4

if (num2>num3):
    f2 = num2
else :
    f2 = num3

if (f1>f2):
    # print(str(f1), 'is greatest' )
    print(f'{str(f1)} is greatest from the given numbers.')
else :
    # print(str(f2),'is greatest' )  
    print(f'{str(f2)} is greatest from the given numbers.')                
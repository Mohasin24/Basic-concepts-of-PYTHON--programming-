#Que :- Write a program to accept 8 numbers from user and display only unique numbers in a list
n=8
uniqueNum = set()
uniqueNum.add(int(input('Enter 1st Number:\n')))
uniqueNum.add(int(input('Enter 2nd Number:\n')))
uniqueNum.add(int(input('Enter 3rd Number:\n')))
uniqueNum.add(int(input('Enter 4th Number:\n')))
uniqueNum.add(int(input('Enter 5th Number:\n')))
uniqueNum.add(int(input('Enter 6th Number:\n')))
uniqueNum.add(int(input('Enter 7th Number:\n')))
uniqueNum.add(int(input('Enter 8th Number:\n')))

if n!=len(uniqueNum):
    print("You have repeated a number twice!")
print(list(uniqueNum))

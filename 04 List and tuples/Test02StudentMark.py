#Que :- write a program to accept the marks of the six students entered by the user and store them in a list

from itertools import count


first = int(input("Enter The Marks Of first Student : "))
second = int(input("Enter The Marks Of second Student : "))
third = int(input("Enter The Marks Of third Student : "))
fourth = int(input("Enter The Marks Of fourth Student : "))
fifth = int(input("Enter The Marks Of fifth Student : "))
sixth = int(input("Enter The Marks Of sixth Student : "))

marks = [first,second,third,fourth,fifth,sixth]

for i in marks:
    for j in marks:
        if j==i>100:
            print(f'You have entered a wrong value please check and try again!\n{j}')
            # for j in marks:
            #     if j==i>100 or j==i<0:
            #             print(j)    
            break

    for j in marks:    
        if j>100:
            print(f'You have entered a wrong value please check and try again!\n{j}')
            # for j in marks:
            #     if j==i>100 or j==i<0:
            #             print(j)    
            break      
else:
        marks.sort()
        print(marks)       
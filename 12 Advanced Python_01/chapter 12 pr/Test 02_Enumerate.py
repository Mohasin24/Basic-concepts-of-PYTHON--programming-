from typing import List

        #0  1  2  3  4   5  6  7  8  9
List1 = [10,20,30,40,50,60,70,80,90,100]

for i, item in enumerate(List1[2:7:2]):
    print(item) 

print('************')

for i, item in enumerate(List1):
    if (i==2 or i==4 or i==6):
        if (i==2):
           print(f'The {i+1}nd element is {item}') 
        else:
            print(f'The {i+1}th element is {item}')     
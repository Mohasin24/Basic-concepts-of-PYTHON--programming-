#Continue Statement:
'''
continue is used to stop the current iteration of the loop and continue 
with the next one. It instructs the program to skip this iteration
'''

#Example:

for i in range(0,5):
    if i == 2:  #if i=2 then the 2 will skip by the loop and further it gets executed until the end
        continue
    print(i)
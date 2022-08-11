#Break : 
'''
break is used to come out of the loop when encountered it instructs
the program to exit the loop now
'''
#Example:
 
for i in range (1,50):
    print(i)
    if i == 20:
        break
    
else:
    print("This loop has been ended!")  
'''
here else will not get executed bcuz the loop did not ended succesfully completed
it has ended at 20 
'''     
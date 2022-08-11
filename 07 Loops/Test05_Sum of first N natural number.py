num = int(input('enter a number:\n'))

if num<0:       #natural number is greater than 0 and non-negative
    print('entr a positive number')
else:
    print (str(num),'is a natural number') 

sum = 0 #initially sum is 0 
while num>0:
    sum = sum + num  
    num = num -1

print(sum)    

'''
python offers a finally clause which ensures execution of a piece of a code irrespective
of the exection. 
if here 'try' throws an error still our code in 'finally' will get executed 
'''
try:
    a = int(input('Enter a number:\n'))
    print('Result:-')
    c = 1/a
    print(c)
except Exception as e:
    print('Error occured!')
    print(e)
    exit()
finally:
    print('****\nFinally we are done!')    #after exiting the program it still get executed

print('Thanks for using the programmer!') #after exiting the program this  will not get executed

# here what ever happens but still finally gets executed  
# executes regradless pf error or exiting the program finally gets executed       

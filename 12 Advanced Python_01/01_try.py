'''
There are many built in exceptions which are raised in python when something goes wrong.
Exeptions in python can be handled using a try statement. The code which handle exception 
is written in except clause

syntax:=

try:
    #code which might throw an error

except Exception as e:
    print (e)
'''

while(True): #infinite loop
    print('Enter q to quit.')    
    a = input('Enter a number:\n')
    if a=='q':
        break
    else:
        try:
            a=int(a)
            if a>=6:
                print('You entered a number greater than 6!')
                
            else:
                print('You entered a number less than six please enter a number gtreater than 6') 
            print("-------")       
        except Exception as e:
            print(f'Your input resulted following error:\n{e}')    
            print("-------")
print('Thanks for playing this game!')        

'''
When exeption is handled the code flow continues without program interruption
'''
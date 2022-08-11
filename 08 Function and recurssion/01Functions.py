#Functions :-
'''
    A function is a group of statement performing a specific task.
    When a program gets bigger in size and its complexity grows it get difficult for a 
programmer to keep track on which piece of code is doing what.
    A function can be resused by the programmer in a given program any number of time.
'''
#Example: 

def percentage(marks):  #return is a fuction which execute the operation defined in it whenever a fucntion is called
    # return (((marks[0] + marks[1]+ marks[2] + marks[3])/400)*100)
    return (sum(marks)/400*100)

marks1 = [45,55,89,75]
#here we have called the func
print('The percentages are:\n',percentage(marks1))

marks2 = [45,98,66,27]
print('The percentages are:\n',percentage(marks2))

marks3 = [67,38,84,92]
print('The percentages are:\n',percentage(marks3))


#Function Call : 
'''
Whenever we want to call a function we put the name of the function followed by parenthesis
func() this is called function call
'''

#Function Definition :
'''
The part containing the exact set of instruction which are executed during the function call.
'''
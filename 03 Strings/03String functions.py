story ='''once upon a time I'm learning to code and started with python language'''

#String Functions 

#Length Func.
print (len(story)) #output will be length of whole str i.e. 69
print('-----')

#end func.
print (story.endswith("language")) #it will give output as a T/F
print('-----')

#count func.
print(story.count("a")) 
print('-----')
'''it will give you number how many,
times this character is used in str,
case sensitive'''

#Capitalise func.
print(story.capitalize())  
print('-----')                       
'''Return a capitalized version of the string.
More specifically, make the first character have 
upper case and the rest lower case.'''

#Find func.
print(story.find("time"))
print('-----')
'''it will give the number of index from which this word starts if not found it
will give -1, it only gives first occurance of the word if a word is repeated
it ingnores it'''

#Replace func.
print(story.replace("once","Second"))
print('-----')
'''
this func will replace old word with new word it will repalces all the words
in the string not the only one word '''
 #we can also use variables to replace a string or word

#Upper
print(story.upper()) 
print('-----')
'''
This will make whole string upper case
'''
#Lower
print(story.lower())
print('-----')
'''
This will make whole string in lower case
'''

#Strip func.:
m = '    My name is Mohasin    '
print(m)
print(m.strip())

'''
Strip function removes the extra spaces in a string
'''
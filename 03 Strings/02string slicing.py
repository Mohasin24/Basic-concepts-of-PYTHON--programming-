
#String Indexing & slicing
#A string in python can be sliced for getting a part of the string
#Example

#numbering  0  1  2  3  4  5  6
#   name = "m  o  h  a  s  i  n" length(6)
#numbering: -7 -6 -5 -4 -3 -2 -1
# slicing always include start index and exclude end index
name = "MOHASIN"
    
print (name[0])
print (name[2])
print (name[-7])
print (name[1:4]) #it will include 1st index and exclude 4th index
print (name[:5]) #if you left first place blank it will automatically replace it with 0
print (name[2:]) #if you left last place blank it will automatically replace it with -1   or last no. of str and it include last index
print (name[:7]) # it wll print whole str
print (name[0:]) # it wll print whole str
print (name[:])  # it wll print whole str
    
# name[3] = "mk" --> does not work i.e str is immutable
# syntax for Str Slicing = name[index start : index end:skip value] 
# here first index included and last excluded if given

#slicing with skip value
   
word = "PYTHON"

print (word[-1::-2]) #it will print str in reverse order with a skip value
print (word[0::2]) 
#the output will be PTO as we added 2 it will skip every second character after
# if we add 3 it will skip 2 character after every charater
   

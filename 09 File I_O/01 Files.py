'''
    The random access memory is volatile and all its
contents are last once a program terminates.
In order to persist the data forever we use files.
    A file is data stored in a storage device. A 
python program can talk to the file by reading content
from it and writing content to it 
'''
#Types of files:-
# 01: Text Files (.txt, .c, etc)
# 02: Binary Files (.jpg, .dat, etc)

# Open Function :-
'''
Python has an open() function for opening files.
It takes 2 parameter : filename and mode
'''
open('file name','r/w' )
#Open is a built in function
#R:-Read W:-Write
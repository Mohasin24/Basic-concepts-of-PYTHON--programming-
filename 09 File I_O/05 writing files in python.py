'''
In order to write a file, we first open it in
write or append mode after which we use the
python f.write() function to write to the file.
'''

f = open('another.txt', 'w')
f.write('I am writing.') #if file is not present already then it will automatically 
# creates the file
f.close()

#for updating a file open it in append mode
f= open('another.txt', 'a')
f.write('\nI am updating a file.') #this line will be added to the end of file
f.close()

# we can use f.write() function multiple times before closing the file i.e. before f.close()
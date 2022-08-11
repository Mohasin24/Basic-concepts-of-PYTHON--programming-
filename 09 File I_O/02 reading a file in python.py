# Use open function to read the content of a file

f = open ('sample.txt', 'r')
# f = open("sample.txt") # by default the mode is 'r'
text = f.read()
# text = f.read(10) # we can also specify the characters in read
print(text)
f.close() #closes the file
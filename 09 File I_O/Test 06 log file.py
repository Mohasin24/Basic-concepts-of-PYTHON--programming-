with open('sample log.txt', 'r') as f:
    file = f.read()
    file = file.lower()

if 'python' in file:
 
    print('Yes, Python is present & the index no. is:-',file.find("python"))
else:
    print('No, Python is not present.')    
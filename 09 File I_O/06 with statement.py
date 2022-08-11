'''
The best way to open and close the flie automatically is the with statement
'''
with open('another.txt', 'r') as f:
    a=f.read()
with open ('another.txt', 'w') as f:
    a=f.write('Hello!')

print(a)
    

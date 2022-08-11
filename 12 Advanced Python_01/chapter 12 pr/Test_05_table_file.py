num = int(input('Enter a number:-\n'))
table = [num*i for i in range(1,11)]
print(str(table))

with open('12 Advanced Python_01/chapter 12 pr/Table.txt','a') as f:
    f.write(str(table))
    f.write('\n')
    
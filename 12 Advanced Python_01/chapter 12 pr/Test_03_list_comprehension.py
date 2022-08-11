num = int(input('Enter a number:-\n'))

# for i in range(1,11):
#     print(f"{num} X {i} = {num*i}")

table = [str(num*i) for i in range(1,11)] 
'''
str(num*i) will make each item of the list into str and then append it to the list
'''
# table = str(table) this will not work
Vtable='\n'.join(table)
print(Vtable)
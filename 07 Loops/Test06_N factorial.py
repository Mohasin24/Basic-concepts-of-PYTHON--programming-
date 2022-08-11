num = int(input('Enter a Number:\n'))
factorial = 1
for i in range (1, num+1):
    factorial=factorial*i

print(f'The factorial of {num} is {factorial}.')    
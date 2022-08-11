n = int(input('Enter a number:\n'))
for i in range(n):
    print('*' * (n-i),end='') #it prints '*' n-i times
    print("+"*i)

    
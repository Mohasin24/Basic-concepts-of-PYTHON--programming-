num = int(input('Enter a number:\n'))

for i in range(1,11):
    i=11-i
    # print(str(num) + 'x' + str(i) + '=' + str(num*i))
    print(f'{num}x{i}={num*i}')
    
    # this is done using f str
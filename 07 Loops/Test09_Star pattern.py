n= 3
for i in range(3):
    for j in range(3):
        # print * completely in first and last row
        # print * only in first and last position in other rows
        if i == 0 or i == 2 or j == 0 or j == 2:
            print('*', end='')
        else:
            print(' ', end='')
    print()
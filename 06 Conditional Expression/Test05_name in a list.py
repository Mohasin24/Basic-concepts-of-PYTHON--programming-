nameList = ['Ravi','Mohasin','Soma', 'Akash', 'Ganesh']
enterName = input('Enter a name:\n')
enterName = enterName.capitalize()
if(enterName in nameList):
    print('This name is present in the list.')
else:
    print('This name is not present in the list.')
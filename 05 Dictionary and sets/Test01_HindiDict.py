#Que :- Write a program to create a dictionary of Hindi words with values as their english translation. Provide user with an option to look it up!

myDict = {

    'Pankha' : 'Fan',
    'Dabba' : 'Box',
    'Vastu' : 'Item'
    #keys     #values

    }
while (True):    
    print('Enter Q to quit')
    # print('Dictionary options are: ', (list(myDict.keys())))
    print(f'Dictionary options are: {(list(myDict.keys()))}')
    a  = input('Enter the Hindi word :\n')
    a = a.capitalize()
    
    if a=="Q":
        exit()  
    # print('The meaning of your word is:', myDict[a]) gives an error if word is not present

    print('The meaning of your word is:', myDict.get(a))

    print("\n")

    '''By adding get method if the word is not present in a dict 
    then it will not throw an error it will give none'''
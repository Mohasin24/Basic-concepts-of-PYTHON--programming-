# Dictionary Methods

myDict= {
    'Fast' : 'In a quick manner',
    'mohasin' : 'a trader',
    'mylist' : [1,2,3,8,9] , #We can add list in a dictionary
    'anotherDict' : {'mohasin':'pasiba'}, #we can add another dictionary in a dictionary
    1: 2
}

# 01_Keys : It will print all the keys of dictionary in the form of list
#And its type will be dict_keys
# aslo we can convert it into a list with help of typecastig
print('\n----------')
print(myDict.keys())
print(type(myDict.keys()))
print(list(myDict.keys()))
print('----------\n')

# 02_Values : we can print values of dictionary
#And its type will be dict_values
# aslo we can convert it into a list with help of typecastig
print(myDict.values())
print(type(myDict.values()))
print(list(myDict.values()))
print('----------\n')

# 03_Items : Prints the (keys,values) for all contains of the dictionary
print(myDict.items())
print(type(myDict.items()))
print(list(myDict.items()))
print('----------\n')
# 04_Update : update dictionary with supplied updated dict
print("Dictionary update")
print(myDict)

updatedDict = {

    'trading' : 'mindset',
    'mk' : 'patel'
}

myDict.update(updatedDict)
print(myDict)
print('----------\n')
# 05_Get : returns the value of specified key if the key is not present in
# the dictionary returns none

print(myDict.get('mohasin2')) #will return none

# print(myDict['mohasin2']) #will return error
#we use .get because it did not throw error if the key is not present in dict.
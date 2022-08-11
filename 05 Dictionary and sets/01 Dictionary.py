#Dictionary : Dictionary is collectionn of key value pairs

myDict= {
      #key          #value
    'Fast' : 'In a quick manner',
    'mohasin' : 'A trader',
    'mylist' : [1,2,3,8,9] , #We can add list in a dictionary
    'anotherDict' : {'mohasin':'pasiba'}, #we can add another dictionary in a dictionary
    # 'mohasin' : 'heeee' #it cannot contain duplicate keys
}



#dictionary is unordered
#we can change dictionary values i.e. dictionary is mutable
#example:

myDict['mylist'] = [2,8,9]

#dictionary is indexed

print(myDict['mylist'])
print(myDict['anotherDict']['mohasin'])
print(myDict['Fast'])
print(myDict['mohasin'])
print(myDict)

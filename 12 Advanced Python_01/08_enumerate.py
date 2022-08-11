list1 = [3,4.5,False,None,'Mohasin']

# index = 0
# for item in list1:
#     print(item,": Index no. is:-",index)
#     index = index + 1

'''
The enumerate function adds counter to an iterable and return it

syntax:-
        for i, item in enumerate(list1):
            print(i,item)    
'''

for index,item in enumerate(list1):
    print(item,": Index no. is:-",index)
a  =[3,6,7,8,9,2,4,23,75,23,123,67]
# b = []

# for item in a:
#     if item%2==0:
#         b.append(item)
# b.sort()
# print(b)

'''
list comprehension is elegant way to create list based on existing list
'''

b = [item for item in a if item%2==0]
b.sort()
print(b)

c = [i for i in a if i%2 !=0]
c.sort()
print(c)


t = [1,4,2,4,1,2,3]
s={i for i in t} #set comprehenssion as elements are not repeated
print(s)

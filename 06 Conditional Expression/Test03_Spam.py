
# a = input('Enter a comment below :\n')

# if ('make a lot of money' in a):
#     spam = True 
# elif('buy now' in a):
#     spam = True
# elif('subscribe this' in a):
#     spam = True
# elif('click this' in a):
#     spam = True
# else :
#     spam = False
# if (spam):
#     print ('This is a spam comment')  
# else: 
#     print('There is no spam comments.')  



a = input('Enter a comment below :\n')
a=a.lower()
spam = ['make a lot of money','buy now','click this','subscribe this']
if a in spam:
    print('Spam')
else:
    print('no')    



             
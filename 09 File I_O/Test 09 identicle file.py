with open('this.txt', 'r') as f :
    content1 = f.read()

with open('copy.txt','r') as f:
    content2 = f.read()

if content1==content2 :
    print('Yes, both the files have similar contents. ')    
else:
    print('Both the files have different contents.') 
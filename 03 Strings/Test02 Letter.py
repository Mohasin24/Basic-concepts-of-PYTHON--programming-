#Que:- Write a program to fill in a letter template given below with name and date:

letter = '''Dear  <|Name|>,
You are selected!,
Date: <|Date|>,
Thank You!
'''
#Solution:-

name = input("Enter Your Name: ")
date = input("Enter Todays Date: ")

name= name.capitalize()
date= date.capitalize()

letter = letter.replace("<|Name|>", name)
letter = letter.replace("<|Date|>", date)
print(letter)


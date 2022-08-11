#QUE:- Create an empty dictionary. Allow 4 friends to enter their favourite languages as values and use their names as keys. Assume that the names are unique.

favLang = {}

a = input('Enter your favourite language Shubham :\n')
b = input('Enter your favourite language Mohasin :\n')
c = input('Enter your favourite language Ravi :\n')
d = input('Enter your favourite language Ankita :\n')

favLang['Shubham'] = a
favLang['Mohasin'] = b
favLang['Ravi'] = c
favLang['Ankita'] = d
print(favLang) 

fav = {
    'A':a,
    'B':b,
    'C':c,
    'D':d   }
print(fav)
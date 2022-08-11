def remove_and_strip(string, word):
    newStr = string.replace(word, '')
    return newStr.strip()

x = '    My name is Mohasin    '

n = remove_and_strip(x,'Mohasin')

print (n)
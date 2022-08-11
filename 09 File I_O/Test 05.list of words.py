words = ['mote', 'kaddu', 'bhalu','donkey']

with open('donkey.txt', 'r') as f:
    con = f.read()
    

for word in words :
    con = con.lower()
    con = con.replace(word, '#####')
    with open('donkey.txt', 'w') as f:
        f.write(con)    
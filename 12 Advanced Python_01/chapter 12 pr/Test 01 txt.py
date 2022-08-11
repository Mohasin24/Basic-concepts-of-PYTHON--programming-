# try:
#     with open('01.txt',"r") as f:
#         f= f.read()
#         print(f)
#     with open('02.txt',"r") as f:
#         f= f.read()
#         print(f)
#     with open('03.txt',"r") as f:
#         f= f.read()
#         print(f)
# except Exception as e:
#     print(e)

def readFile(fileName,mode):
    try:
        with open(fileName,mode) as f:
            print(f.read())
    # except Exception as e:
    #     print(f'File did not opened due to following error:-\n{e}')
    except FileNotFoundError :
        print(f'File {fileName} not found')

readFile('12 Advanced Python_01/chapter 12 pr/01.txt','r')
readFile('12 Advanced Python_01/chapter 12 pr/02.txt','r')
readFile('03.txt','r')
        
    
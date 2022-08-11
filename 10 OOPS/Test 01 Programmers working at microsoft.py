class programmer :
    company = 'Microsoft'
    def __init__(self,name,product):
        self.name = name
        self.product = product

    def getInfo(self):
        print(f'The name of the {self.company} programmer is {self.name} and the product is {self.product}.')

mohasin = programmer('Mohasin','Skype')      
patel = programmer("Patel","GitHub") 
mohasin.getInfo()
print('---------++++++---------')
patel.getInfo()
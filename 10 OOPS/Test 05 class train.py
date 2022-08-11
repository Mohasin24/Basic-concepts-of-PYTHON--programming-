class train:
    def __init__(self,name,fare,seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def getStatus(self) :
        print('*********')
        print(f"The name of the train is {self.name}")
        print(f"The seats available in the train are {self.seats}")  
        print('*********')     

    def fareInfo(self):
        print(f"The price of the train ticket is : Rs.{self.fare}/-")  

    def bookTicket(self):
        if (self.seats >0) :
            print(f"Your ticket is booked! Your seat no. is : {self.seats}")
            self.seats = self.seats - 1
            intercity.fareInfo()
        else:
            print('Sorry this train is full! Kindly try in tatkal')   

    def cancleTicket(self,seatNo):
        pass


intercity = train('Intercity Express : 14015',90,2)
intercity.getStatus()
intercity.bookTicket()

intercity.getStatus()
intercity.bookTicket()

intercity.getStatus()
intercity.bookTicket()

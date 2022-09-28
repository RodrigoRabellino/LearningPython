from People import People

class Client(People): 
    def __init__(self, firstName, lastName, ciNum, phone, address):
        super().__init__(firstName, lastName, ciNum, phone,)
        self.address = address
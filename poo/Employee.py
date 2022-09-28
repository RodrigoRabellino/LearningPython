from People import People

class Employee(People): 
    def __init__(self, firstName, lastName, ciNum, phone, salary):
        super().__init__(firstName, lastName, ciNum, phone,)
        self.salary = salary
    
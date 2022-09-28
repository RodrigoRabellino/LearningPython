class People:
    def __init__(self, firstName, lastName, ciNum, phone):
        self.firstName = firstName
        self.lastName = lastName
        self.ciNum = ciNum
        self.phone = phone
    def __str__(self): 
        return "Name: {} {}, ci: {}".format(self.firstName, self.lastName, self.ciNum)
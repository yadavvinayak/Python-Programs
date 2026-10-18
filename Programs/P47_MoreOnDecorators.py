                                                                             

class BankAccount(object):
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

    @property                                       
    def fullName(self):
        return self.firstName + ' ' + self.lastName

    @fullName.setter
    def fullName(self, name):
        firstName, lastName = name.split(' ')
        self.firstName = firstName
        self.lastName = lastName

if __name__ == '__main__':
    acc = BankAccount('VinayakYadav', 'Yadav')
    print(acc.fullName)                                                                                      

    acc.fullName = 'Jagdish Yadav'
    print(acc.fullName)

                                                   

class Vehicle():

    def __init__(self):                                                      
        print('Calling init')
        self.val = 0
        self.cost = 10000                                                        

    def incrementVehicle(self):
        self.val += 1

car = Vehicle()                        
print('First obj value:',car.val)
car.incrementVehicle()
car.incrementVehicle()
print('First obj value after incrementing:',car.val)        

bike = Vehicle()                                                                
print('Second obj value:',bike.val)



import numpy as np

myArray = np.arange(1, 21)
print(myArray)                                                                                     

myArray = np.arange(10, dtype = 'float')
print(myArray)                                                                 

myArray = np.arange(1, 21, 2)
print(myArray)                                                       

myArray = np.linspace(10, 20, 5)
print(myArray)                                                       

myArray = np.linspace(10, 20, 5, endpoint = False)
print(myArray)                                                  

myArray = np.logspace(1.0, 3.0, num = 10)
print(myArray)

myArray = np.logspace(1.0, 3.0, num = 10, base = 2)
print(myArray)


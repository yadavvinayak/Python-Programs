

import numpy as np

myArray = np.arange(20)
print(myArray)                                                                             

myArray = np.arange(10, 20)                                  
print(myArray)

myArray = np.arange(10, 20, 2)
print(myArray)                                

myArray = np.arange(20)
                                                    
myArray = myArray.reshape(4, 5)
print(myArray)

myArray = myArray.reshape(10, 2)
print(myArray)

print(myArray.shape)                 

print(myArray.ndim)            

print(myArray.size)             

print(myArray.dtype)               

myArray = np.zeros((3, 4))
print(myArray)

myArray = np.ones((3, 4))
print(myArray)

myArray = np.random.rand(3, 4)
print(myArray)


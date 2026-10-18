

myFunc = lambda x, y: x * y  

print(myFunc(2, 3))                                 

print((lambda x, y: x * y)(2, 3))                           

print(type(lambda x, y: x * y))                                      

myList = [i for i in range(10)]

myFunc2 = lambda x: x * x

squares = list(map(myFunc2, myList))
print(squares)                                                                            

print(list(map(lambda x: x * x, myList)))                 


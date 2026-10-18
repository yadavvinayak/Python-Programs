                                                                                       

                  
                                                            
                                                                 
                                                                          
                                                                                             

numbers = []
for i in range(10):
    numbers.append(i)
print(numbers)                                              

                                                                               
                                                                                                        

                     
numbers = [i for i in range(10)]
print(numbers)                                              

                              
squares = [i * i for i in range(10)]
print(squares)                                                    

                  
squares = []
for i in range(10):
    squares.append(i * i)

            
odds = [i for i in numbers if i % 2 != 0]
print(odds)                                  

                  
odds = []
for i in numbers:
    if i % 2 != 0:
        odds.append(i)

                                             
def isSqaure(x):
    import math
    sqrt = int(math.sqrt(x))
    return x == sqrt * sqrt

squares = [x for x in range(100) if isSqaure(x) == True]
print(squares)                                                   

                              
pairs = [[x, x * x] for x in numbers]
print(pairs)                                                                                                       

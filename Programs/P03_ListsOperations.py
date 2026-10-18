                                                          

                               

myList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                                   
                                   

             
print('Original List:',myList)
print('First Element:',myList[0])                                                                 
print('Element at 2nd Index position:',myList[2])                                    
print('Elements from 0th Index to 4th Index:',myList[0: 5])                                                                                            
print('Element at -7th Index:',myList[-7])                                            

                               
myList.append(10)
print('Append:',myList)

                                          
print('Index of element \'6\':',myList.index(6))                              

                 
myList.sort()

                    
print('Poped Element:',myList.pop())

                                                     
myList.remove(6)
print('After removing \'6\':',myList)

                                          
myList.insert(5, 6)
print('Inserting \'6\' at 5th index:',myList)

                                                       
print('No of Occurences of \'1\':',myList.count(1))

                                                                                
myList.extend([11,0])
print('Extending list:',myList)

                  
myList.reverse()
print('Reversed list:',myList)

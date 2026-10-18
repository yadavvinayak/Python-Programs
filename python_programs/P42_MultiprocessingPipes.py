                                                                                         

from multiprocessing import Process, Pipe

def parentData(parent):
    ''' This function sends the data for the child process '''
    parent.send(['Hello'])
    parent.close()

def childData(child):
    ''' This function sends the data for the parent process '''
    child.send(['Bye'])
    child.close()

if __name__ == '__main__':
    parent, child = Pipe()                           
    process1 = Process(target = parentData, args = (parent, ))                                                 
    process2 = Process(target = childData, args = (child, ))                                                  
    process1.start()                                               
    process2.start()                                             
    print(parent.recv())                                                        
    print(child.recv())                                                            
    process1.join()                                                                    
    process2.join()

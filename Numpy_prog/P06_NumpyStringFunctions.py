
import numpy as np

abc = ['abc']
xyz = ['xyz']

print(np.char.add(abc, xyz))                

print(np.char.add(abc, 'pqr'))              

print(np.char.multiply(abc, 3))                

print(np.char.center(abc, 20, fillchar = '*'))                            

print(np.char.capitalize('hello world'))                     

print(np.char.title('hello how are you?'))                          

print(np.char.lower(['HELLO','WORLD']))                            

print(np.char.upper('hello'))                          

print(np.char.split('VinayakYadav'))                                       
print(np.char.split('2017-02-11', sep='-'))                           

print(np.char.join(':','dmy'))                         

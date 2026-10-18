
                                                                                      

                                                                                                   
                                                                                                   

                                              

from Crypto.PublicKey import RSA
from Crypto import Random

randomGenerator = Random.new().read
                                           
                          
key = RSA.generate(1024, randomGenerator)                                      
print(key)                                                    
print(key.publickey())                                       

                             
publicKey = key.publickey()
encryptedData = publicKey.encrypt('My name is VinayakYadav'.encode('utf-8'), 32)
print(encryptedData)

                              
decryptedData = key.decrypt(encryptedData)
print(decryptedData)

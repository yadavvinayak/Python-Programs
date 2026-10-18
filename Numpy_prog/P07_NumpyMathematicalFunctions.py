
import numpy as np

angles = np.array([0, 30, 45, 60, 90, 180, 360])

print(np.sin(angles * np.pi/180))

print(np.cos(angles * np.pi/180))

print(np.tan(angles * np.pi/180))

sine = np.sin(angles * np.pi/180)
sineinv = np.arcsin(sine)
                              
print(np.degrees(sineinv))

print(np.around(sine, 4))                                                                  

print(np.floor(sine))                                          

print(np.ceil(sine))                                           

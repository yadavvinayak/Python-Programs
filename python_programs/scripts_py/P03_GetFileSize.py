                                                                                                   

import os                                
directory = '/home/vinayak/Documents/GITs/Python-Programs/Scripts'                                                         
dir_size = 0                       

fsizedicr = {'Bytes': 1, 'Kilobytes': float(1)/1024, 'Megabytes': float(1)/(1024*1024), 'Gigabytes': float(1)/(1024*1024
                                                                                                               *
                                                                                                               1024)}

for (path, dirs, files) in os.walk(directory):                                                                                                                           
    for file in files:                                                 
        filename = os.path.join(path, file)
        dir_size += os.path.getsize(filename)                                                                         

for key in fsizedicr:                                        
    print ("Folder Size: " + str(round(fsizedicr[key]*dir_size, 2)) + " " + key)                                                           

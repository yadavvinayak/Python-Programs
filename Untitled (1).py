                     

file = open('social.txt', 'r')
data = file.read()

file.close()

print(file.closed)  

with open('social.txt', 'r') as file:
    data = file.read()
    
print(file.closed)

with open('something.txt', 'a') as file:
    file.write('MMCOE - yethe bahutanche hith!')

with open('social.txt', 'r') as fd:
    data = fd.read(6)                                                  
    
print(data)

import os

print(os.getcwd())

print('Original Directory:', os.getcwd())
os.chdir('/home/vinayak/Documents/Notebooks')
print('Current Directory:', os.getcwd())

print(os.listdir())

files = []

files = os.listdir()

for file in files: 
    if os.path.isfile(os.path.abspath(file)):
        print('File:', file)
        
for file in files: 
    if os.path.isdir(os.path.abspath(file)):
        print('Dir:', file)

os.chdir('/home/vinayak/Documents/PythonLecture/Naruto/Directory0')

for i in range(10):
    os.mkdir('Directory' + str(i) + str(i))                      
    os.chdir('Directory' + str(i) + str(i))                             
    with open('something.txt', 'w') as file:
        file.write('Text')
    os.chdir('/home/vinayak/Documents/PythonLecture/Naruto/Directory0')

os.chdir('/home/vinayak/Documents/PythonLecture/')

mylist = ['VinayakYadav', 1, 3, 4.0]
print(mylist)

word_to_check = 'hilarious'

with open('social.txt', 'r') as file:
    data = file.read()
    
for line in data.split('\n'):
    if word_to_check in line:
        print('True')
        print(line)
        
print(len(data.split('\n')))

os.chdir('/home/vinayak/Documents/PythonLecture')
with open('social.txt', 'r') as file:
    data = file.read()
    
char = 'M'
                     
print(data.lower().count(char.lower()))

with open('social.txt', 'r') as file:
    data = file.read()
    
char = input('Enter a character of your choice:')

print(data.lower().count(char))

string = 'My namename is VinayakYadav'
print(string.count('name'))                  

import numpy
import scipy
import matplotlib


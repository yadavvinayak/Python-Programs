#qwention on slicing
# take input and print middle 3 characters, last 2 characters
#green 5
str= input("Enter a value:")
mid= len(str)//2
output1= str[mid-1:mid+2]
print(output1)
output2= str[-2:]
print(output2)
                                                                    
student= {"name":"Vinayak", "age":31,"city":"Pune", "Roll no.":31}
print(type(student))
print(student)
print(student["name"])
print(student["age"])
print(student["Roll no."])
student["city"]="Benglore"
print(student)
student["favSub:"]= "Programming"
print(student)
student.pop("favSub:")
print(student)
print(student.keys())
print(student.values())
print(student.items())
print(student.get("name"))
print(student.update({"age": 30}))
print(student)
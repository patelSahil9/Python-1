class employee:
    name="sahil"  #class attribute
    age=21
    slalary=50000
    
sahil = employee()
sahil.name="Sahil Patel"   #object attribute
print(sahil.name)
rohan = employee()
rohan.name="rohan Patel"
print(rohan.name)

#here name is class attribute but when we assign value to object attribute it overrides the class attribute for that object only.
print(employee.name)  #accessing class attribute using class name
class employee:
    name="sahil"  #class attribute
    age=21
    slalary=50000
    
        #dunder method which is called automatically when an object is created.(like check last line nigga=employee()) 
    def __init__(self):
        print("Employee object created.")
    
    def __init__(self,name,age,slalary):
        print("Employee object created.")
        self.name=name
        self.age=age
        self.slalary=slalary
        
    def get_info(self):
        #self is used to refer to the current object. we can use anyhting inplace of self.
        print(f"Name: {self.name}, Age: {self.age}, Salary: {self.slalary}")
    @staticmethod   #it will mark this method as static method.its also called decorator.it dont need object reference.
    def greet(self):
        print(f"Hello {self.name}, welcome to the company!")
    
sahil = employee("sahil",21,50000)
sahil.name="Sahil Patel"   #object attribute
sahil.get_info()
#when we use object attribute it overrides the class attribute for that object only in all cases.like priority is given to object attribute.
# nigga = employee()

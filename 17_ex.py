#store microsoft company's employees details
class employee:
    company="Microsoft"
    def __init__(self,name,salary,age,pincode):
        self.name=name
        self.salary=salary
        self.age=age
        self.pincode=pincode
p= employee("sahil",50000,21,1234)
print(p.name,p.salary,p.age,p.pincode)
r= employee("rohan",50000,21,1234)
print(r.name,r.salary,r.age,r.pincode)
sr= employee("suresh",50000,21,1234)
print(sr.name,sr.salary,sr.age,sr.pincode)

#calculator

class calculator:
    @staticmethod
    def hello():
        print("hello")
    def __init__(self,x):
        self.x=x
        def square(self):
            print("square=",self.x*self.x)
        def cube(self):
            print("cube=",self.x*self.x*self.x)
            
    a.hello()
#class with attribute
class Demo:
    a=10
o=Demo()
print(o.a)
o.a=888
print(o.a)
print(Demo.a)
class Train:
    def book(self, trainNo,fro,to):
        print(f"Train number {trainNo} from {fro} to {to} is booked")
    def status(self,trainNo):
        print(f"Train is booked in train {trainNo} is running on time")
    def getFare(self,trainNo,fro,to):
        print(f"Train number {trainNo} from {fro} to {to} fare is 500rs")
        
#we can use self.fro method when we use init method dunder method
t=Train()
t.book(12345,"Delhi","Mumbai")
t.status(12345)
t.getFare(12345,"Delhi","Mumbai")

class Names:
    def __init__(slf,name1,name2,name3):
        slf.name1=name1
        slf.name2=name2
        slf.name3=name3
    def printNames(slf):
        print("Name 1 is:",slf.name1)
        print("Name 2 is:",slf.name2)
        print("Name 3 is:",slf.name3)
n=Names("Sahil","Rohan","Suresh")
n.printNames()
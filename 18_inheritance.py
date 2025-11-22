class info:
    def __init__(self, name, age, addr):
        self.name = name
        self.age = age
        self.addr = addr
        
    def show_info(self):
        print(f"this is {self.name} and the age is {self.age} and address is {self.addr}")

class sahil(info):
    def __init__(self, name, age, addr, color, canrun):
        super().__init__(name, age, addr)
        self.color = color
        self.canrun = canrun
    
    def show_details(self):
        self.show_info()
        print(f"his color is {self.color} and he {self.canrun}")

a = sahil("sahil", "21", "dehgam", "white", "can run")
a.show_details()

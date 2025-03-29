class Vehicle:
    def __init__(self,make,model,trim,top_speed,rpm):
        self.make = make
        self.model = model
        self.trim = trim
        self.top_speed = top_speed
        self.rpm = rpm
    
    def display(self):
        print(f"make: {self.make}")
        print(f"model: {self.model}")
        print(f"trim: {self.trim}")
        print(f"top_speed: {self.top_speed}")
        print(f"rpm: {self.rpm}")
    
v1= Vehicle("toyota","corolla","x",180,4000)
v2= Vehicle("ferrari","458","italia",300,9000)
v1.display()
v2.display()
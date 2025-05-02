class Vehicle:
    def __init__(self,name,max_speed,milage):
        self.name = name
        self.max_speed = max_speed
        self.milage = milage

class Bus(Vehicle):
    pass

school_bus=Bus("school bus",120,12)
print(f"vehicle name is {school_bus.name}, max speed is {school_bus.max_speed}, milage is {school_bus.milage}")
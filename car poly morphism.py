class BMW:
    def __init__(self, model_name, fuel, speed):
        self.model_name = model_name
        self.fuel = fuel
        self.speed = speed

    def fuel_type(self):
        print(f"{self.model_name} uses {self.fuel} fuel.")

    def max_speed(self):
        print(f"{self.model_name} has a top speed of {self.speed} km/h.")

    def model(self):
        print(f"This is a BMW model: {self.model_name}")


class Ferrari:
    def __init__(self, model_name, fuel, speed):
        self.model_name = model_name
        self.fuel = fuel
        self.speed = speed

    def fuel_type(self):
        print(f"{self.model_name} uses {self.fuel} fuel.")

    def max_speed(self):
        print(f"{self.model_name} has a top speed of {self.speed} km/h.")

    def model(self):
        print(f"This is a Ferrari model: {self.model_name}")



bmw_car = BMW("M4 Competition", "Petrol", 290)
ferrari_car = Ferrari("SF90 Stradale", "Hybrid", 340)

bmw_car.model()
bmw_car.fuel_type()
bmw_car.max_speed()

print()

ferrari_car.model()
ferrari_car.fuel_type()
ferrari_car.max_speed()
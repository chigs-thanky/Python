class Car:
    wheels = 4

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.__speed = 0

    def start(self):
        print(f"{self.brand} {self.model} started")

    def accelerate(self):
        self.__speed += 20

    def show_speed(self):
        print("Speed:", self.__speed)


class ElectricCar(Car):
    def __init__(self, brand, model, battery):
        super().__init__(brand, model)
        self.battery = battery

    def start(self):
        print(f"{self.brand} {self.model} started silently")


car1 = Car("Toyota", "Camry")
tesla = ElectricCar("Tesla", "Model 3", "75 kWh")

car1.start()
tesla.start()

car1.accelerate()
car1.show_speed()

print("Wheels:", tesla.wheels)
print("Battery:", tesla.battery)
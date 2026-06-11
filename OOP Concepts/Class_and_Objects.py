# define a class
class Car:
    wheels = 4  # Class attribute (shared by all cars)
    engine = "V8" # Class attribute (shared by all cars)

    def __init__(self, brand, model):
        self.brand = brand  # Instance attribute
        self.model = model  # Instance attribute
        self.__speed = 0      # Private attribute (Encapsulation)

    def start(self):
        print(f"{self.brand} is starting")

    def stop(self):
        print(f"{self.brand} is stopping")

car1 = Car("Toyota", "Hyryder")
car2 = Car("Honda", "City")
car3 = Car("Tata", "Punch")

print(car1.brand)    # Toyota
print(car2.brand)    # Honda
print(car1.wheels)   # 4
print(car2.wheels)   # 4
print(car3.model)    # Punch
car1.start()
car1.stop()
car2.start()
car3.start()
print(f"\n{car1.brand} - {car1.model} - {car1.engine}")
print(f"{car2.brand} - {car2.model} - {car2.engine}")
print(f"{car3.brand} - {car3.model} - {car3.engine}")




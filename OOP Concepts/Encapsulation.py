class Car:
    def __init__(self, brand):
        self.brand = brand
        self.__speed = 0  # private attribute

    def accelerate(self):
        self.__speed += 10

    def show_speed(self):
        print(f"{self.brand} - Speed: {self.__speed} kmph")

car1 = Car("Audi")
car2 = Car("BMW")

car1.accelerate()
car1.show_speed()
car1.accelerate()
car1.accelerate()
car1.show_speed()

print(car2.brand)
print(car1.brand)
print(car2.__speed) # AttributeError: 'Car' object has no attribute '__speed'
